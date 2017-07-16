from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserCreateForm, UserProfileForm, UserEditForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import UserProfile
from crafts.models import CraftPost
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register(request):

    if request.method == 'POST':
        print(request.POST)
        print("WTF")
        user = request.POST
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            if 'picture' in request.FILES:
                picture=request.FILES['picture']
            else:
                picture = None
            userprofile = UserProfile(user=user, location=request.POST['location'], picture=picture, hobby=request.POST["hobby"])
            userprofile.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', { 'form': form })


@login_required
def profile_edit(request):
    userprofile = UserProfile.objects.get(user=request.user)
    user = userprofile.user
    if request.method =="POST":
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.save()
            return redirect('/myprofile')
        else:
            print("something")
    else:
        form = UserProfileForm(instance=userprofile)

    return render(request, 'profiles/profile_edit.html', {'form': form })

#currently not using so Im commenting it out, it does it automatically in django
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')

@login_required
def user_profilelist(request):
    userprofiles = UserProfile.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(userprofiles, 10)
    try:
        userprofiles = paginator.page(page)
    except PageNotAnInteger:
        userprofiles = paginator.page(1)
    except EmptyPage:
        userprofiles = paginator.page(paginator.num_pages)
    return render(request, 'profiles/user_profilelist.html', {'userprofiles': userprofiles})

@login_required
def myprofile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    craftposts= CraftPost.objects.filter(author=request.user).filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(craftposts, 6)
    try:
        craftposts = paginator.page(page)
    except PageNotAnInteger:
        craftposts = paginator.page(1)
    except EmptyPage:
        craftposts = paginator.page(paginator.num_pages)
    return render(request, 'profiles/user_profile.html', {'userprofile': userprofile,'craftposts': craftposts})


@login_required
def user_profiles(request, id):
    userprofile = UserProfile.objects.get(id=id)
    craftposts = CraftPost.objects.filter(author=userprofile.user.id).filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(craftposts, 6)
    try:
        craftposts = paginator.page(page)
    except PageNotAnInteger:
        craftposts = paginator.page(1)
    except EmptyPage:
        craftposts = paginator.page(paginator.num_pages)    
    return render(request, 'profiles/user_profile.html', {'userprofile': userprofile,'craftposts': craftposts})


