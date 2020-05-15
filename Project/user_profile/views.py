from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm ######, UserChangeForm NEED LATER???
from django.contrib.auth.decorators import login_required
from user_profile.models import Profile, ProfileImage, History
from user_profile.forms.profile_form import ProfileForm


# Create your views here.
@login_required
def get_profile_by_id(request):
    return render(request, 'user_profile/profile.html', {
        'user': request.user
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user_profile/register.html', {
        'form': UserCreationForm()
    })

@login_required
def update_profile(request):
    profile = Profile.objects.filter(user_id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user
            profile.save()
            return redirect('profile_page')
    return render(request, 'user_profile/update_profile.html', {
        'form': ProfileForm(instance=profile)
    })


@login_required
def history(request):
    search_history = list(History.objects.filter(user_id_id=request.user.id))
    return render(request, 'user_profile/history.html', {
        'history': search_history
    })

