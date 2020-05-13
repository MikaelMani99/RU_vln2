from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm ######, UserChangeForm NEED LATER???
from user_profile.models import User, UserImage, History

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

