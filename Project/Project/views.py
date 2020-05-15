from django.shortcuts import redirect
from django.shortcuts import render

def view_404(request, *args, **argv):
    return render(request, '404.html', {
        'user': request.user
    })

def view_500(request, *args, **argv):
    return redirect('500.html')