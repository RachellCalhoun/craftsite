from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserCreateForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import UserProfile
from crafts.models import CraftPost
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            userprofile = UserProfile(user=user, location=request.POST['location'], picture=request.POST["picture"], hobby=request.POST["hobby"])
            userprofile.save()
            login(request, user)
            messages.add_message(request, messages.INFO, 'Thank you for registering!', 'message register-success')
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', { 'form': form })

@login_required
def profile_edit(request):
    userprofile = UserProfile.objects.get(user=request.user)
    user = userprofile.user
    if request.method =="POST":
        form = UserCreateForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            return redirect('user_profile', user=userprofile.user)
            
    else:
        form = UserCreateForm(instance=userprofile)
    return render(request, 'profiles/profile_edit.html', {'form': form})

#currently not using so Im commenting it out, it does it automatically in django
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')

@login_required
def user_profiles(request):
    userprofile = UserProfile.objects.get(user=request.user)
    craftposts = CraftPost.objects.filter(author=request.user).order_by('-created_date')
    return render(request, 'profiles/user_profile.html', {'userprofile': userprofile,'craftposts': craftposts})


@login_required
def user_profilelist(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'profiles/user_profilelist.html', {'userprofiles': userprofiles})

