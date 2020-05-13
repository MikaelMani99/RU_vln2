from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm ######, UserChangeForm NEED LATER???
from django.contrib.auth.decorators import login_required
from user_profile.models import Profile, ProfileImage, History

# Create your views here.
def get_profile_by_id(request, id):

    return render(request, 'user_profile/profile.html', {
        'user': get_object_or_404(User, pk=id)
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
def history(request):
    search_history = list(History.objects.filter(user_id_id=request.user.id))
    return render(request, 'user_profile/history.html', {
        'history': search_history
    })

