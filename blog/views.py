from django.shortcuts import render
from .models import Post
from evaluate.models import *
from django.contrib.auth import get_user_model
user = get_user_model()

def home(request):  
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        context = { 'posts': Post.objects.all(),'ratings':Ratings.objects.all().order_by('-time') }
        # context = { 'posts': Post.objects.all()}
        return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
