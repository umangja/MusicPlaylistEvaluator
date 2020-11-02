from django.shortcuts import render
from .models import Post
from evaluate.models import *
from django.contrib.auth import get_user_model
from MusicPlayer.constants import *
from users.models import *
from MusicPlayer.constants import APP_DESCRIPTION,DEVELOPERS
user = get_user_model()

def home(request):  
    
    TL = TIMELIMIT.objects.all()
    if TL.count() == 0:
        TL = TIMELIMIT(timeLimit=10)
        TL.save()

    Siz = SIZES.objects.all()
    if Siz.count() == 0:
        Sizes = SIZES(setSize=1000,playlistSize=50,GapSize=10)
        Sizes.save()


    if request.user.is_authenticated:
        allUsers   = user.objects.all(); 
        TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
        return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'allUsers':allUsers})
    else:
        context = { 'posts': Post.objects.all(),'ratings':Ratings.objects.all().order_by('-time') }
        return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About','description':APP_DESCRIPTION,'developers':DEVELOPERS})
