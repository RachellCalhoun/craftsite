from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from PIL import Image
from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class CraftPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = get_thumbnail(self.image, '500x600', quality=99, format='JPEG')
    #     super(CraftPost, self).save(*args, **kwargs)
    def save(self):
        # Opening the uploaded image
        im = Image.open(self.photo)

        output = BytesIO()

        # Resize/modify the image
        # im = im.resize((500, 500))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=10)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.photo.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(output), None)
        print(self.photo)
        super(CraftPost, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def unapproved_comments(self):
        return self.comments.filter(approved_comment=False)


class Comment(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, default="anon")
    craftpost = models.ForeignKey(CraftPost, related_name='comments')
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Category(models.Model):
    order = models.PositiveIntegerField(help_text="Enter a number.")
    title = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    order = models.PositiveIntegerField(help_text="Enter a number.")
    title = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
