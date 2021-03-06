from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 
                          'account/register_done.html', 
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                  'account/register.html', 
                  {'user_form': user_form})           

@login_required
def profile(request):
    posts = request.user.blog_posts.all()
    return render(request, 
                  'account/profile.html', 
                  {'posts': posts})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, 
                                       data=request.POST, 
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile successfully updated')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        messages.error(request, 'Error updating your profile')
    return render(request, 
                  'account/edit.html', 
                  {'user_form': user_form, 
                   'profile_form': profile_form})                                                                                                                                                 