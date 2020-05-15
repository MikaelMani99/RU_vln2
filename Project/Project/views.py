from django.shortcuts import redirect

def view_404(request, exception=None):
    # make a redirect to homepage
    return redirect('/')