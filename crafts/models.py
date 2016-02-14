from django.db import models
from django.utils import timezone
# Create your models here.

class CraftPost(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	photo = models.ImageField(blank=True, null=True)
	link = models.URLField(max_length=200, blank=True, null=True)
	FOOD = "Food"
	CRAFT = "Craft"
	POSTCATEGORY = (
		(CRAFT, 'Craft'),
		(FOOD, 'Food'),
		)
	postcategory = models.CharField(max_length=5, choices=POSTCATEGORY, default=CRAFT)


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
	author = models.ForeignKey('auth.User')
	craftpost = models.ForeignKey(CraftPost, related_name='comments')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
