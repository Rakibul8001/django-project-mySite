from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'profile/home.html')

def about(request):
    return render(request, 'profile/about.html')

@login_required
def userProfile(request):
    user = request.user
    return render(request, 'profile/profile.html',{
        'user': user
    })
