from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'captain/index.html')

def profile(request):
    return render(request, 'captain/profile.html')