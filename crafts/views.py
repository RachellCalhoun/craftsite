from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import CraftPost
from .forms import CraftForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def craft_list(request):
	craftposts = CraftPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'crafts/craft_list.html', {'craftposts': craftposts})

def craft_detail(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	return render(request, 'crafts/craft_detail.html',{'craftpost': craftpost})

@login_required
def craft_new(request):
	if request.method == "POST":
		form = CraftForm(request.POST)
		if form.is_valid():            
			craftpost = form.save(commit=False)
			craftpost.author = request.user
			craftpost.save()
			return redirect('craft_detail', pk=craftpost.pk)
	else:
		form = CraftForm()
	return render(request, 'crafts/craft_edit.html', {'form': form})

@login_required
def craft_edit(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	if request.method =="POST":
		form = CraftForm(request.POST, instance=craftpost)
		if form.is_valid():
			craftpost = form.save(commit=False)
			craftpost.author = request.user
			craftpost.save()
			return redirect('craft_detail', pk=craftpost.pk)
	else:
		form = CraftForm(instance=craftpost)
	return render(request, 'crafts/craft_edit.html', {'form': form})

@login_required
def craft_draft_list(request):
	craftposts = CraftPost.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'crafts/craft_draft_list.html', {'craftposts':craftposts})

@login_required
def craft_publish(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	craftpost.publish()	
	return redirect('crafts.views.craft_detail', pk=pk)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

@login_required
def craft_remove(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	craftpost.delete()
	return redirect('crafts.views.craft_list')

def add_comment_to_craft(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.save()
			return redirect('crafts.views.craft_detail', pk=craftpost.pk)
	else:
		form = CommentForm()
	return render(request, 'craft/add_comment_to_post.html', {'form': form})