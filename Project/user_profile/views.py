from django.shortcuts import render

from user_profile.models import User, UserImage, History

# Create your views here.
def get_profile_by_id(request, id):

    return render(request, 'captain/profile.html', {
        'user': get_object_or_404(User, pk=id)
    })
