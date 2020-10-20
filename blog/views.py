from django.shortcuts import render
from .models import Post
from evaluate.models import *
from django.contrib.auth import get_user_model
from MusicPlayer.constants import *
from users.models import *
user = get_user_model()

def home(request):  
    if request.user.is_authenticated:
        allUsers   = user.objects.all(); 
        TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
        return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'allUsers':allUsers})
    else:
        context = { 'posts': Post.objects.all(),'ratings':Ratings.objects.all().order_by('-time') }
        # context = { 'posts': Post.objects.all()}
        return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
