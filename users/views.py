from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *
from evaluate.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from MusicPlayer.constants import *
user = get_user_model()


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def showAllRating(request):
    current_user = request.user
    ratings = Ratings.objects.all().order_by('-time')

    playlistNames = []
    algoNames    = []

    for rating in ratings:
        playlistName = rating.playlistId.playlistName
        algoName    = rating.algoId.algoName

        playlistNames.append(playlistName)
        algoNames.append(algoName)
    return render(request,'users/showAllRatingWithTimming.html',{'ratings':ratings, 'playlistNames':playlistNames, 'algoNames':algoNames,})

@login_required
def showAllRatingForParticularUser(request):
    if request.method == "POST":
        asked_user = request.POST.get('allUsers')
        ratings = Ratings.objects.filter(userId=asked_user).order_by('-time')

        playlistNames = []
        algoNames    = []

        for rating in ratings:
            playlistName = rating.playlistId.playlistName
            algoName    = rating.algoId.algoName

            playlistNames.append(playlistName)
            algoNames.append(algoName)

        return render(request,'users/showAllRatingWithTimming.html',{'ratings':ratings, 'playlistNames':playlistNames, 'algoNames':algoNames,})
    else:
        TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
        return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT})


@login_required
def adminSetting(request):
    TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
    SETSIZE   = SIZES.objects.all()[0].setSize
    PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
    GAPSIZE      = SIZES.objects.all()[0].GapSize
    return render(request, 'users/settings.html',{'timeLimit':TIMELIMITs,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE})


@login_required
def updateTimeLimit(request):
    if request.method == 'POST':
        newTimeLimit = int(request.POST.get('timeLimit'))
        if newTimeLimit<5 or newTimeLimit>300 :
            mess = "Time Limit should be >=5 and <=300"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            SETSIZE   = SIZES.objects.all()[0].setSize
            PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})
        else:
            TIME_LIMIT=newTimeLimit
            timelimit = TIMELIMIT.objects.all()[0]
            timelimit.timeLimit=newTimeLimit
            timelimit.save()
            mess = "Time Limit Updated Succesfully"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            SETSIZE   = SIZES.objects.all()[0].setSize
            PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})
    else:
        TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
        SETSIZE   = SIZES.objects.all()[0].setSize
        PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
        GAPSIZE      = SIZES.objects.all()[0].GapSize
        return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE})




@login_required
def updatePlaylistSize(request):
    SETSIZE   = SIZES.objects.all()[0].setSize
    if request.method == 'POST':
        newPlaylistSize = int(request.POST.get('playlistSize'))
        newGapSize      = int(request.POST.get('gapSize'))
        if newPlaylistSize<10 or (newPlaylistSize%newGapSize)!=0 or newPlaylistSize/newGapSize>10 or newPlaylistSize/newGapSize<=0 or newPlaylistSize>SETSIZE :
            mess = "playlist size should be >=10 and multiple of " + str(newGapSize) + " and maximum there can be 10 ratings and " +"Playlist Size should be less then Set Size"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})
        else:
            siz = SIZES.objects.all()[0]
            siz.playlistSize=newPlaylistSize
            siz.GapSize=newGapSize
            siz.save()
            mess = "Playlist Size Updated Succesfully"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})
    else:
        TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
        PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
        GAPSIZE      = SIZES.objects.all()[0].GapSize
        return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE})




@login_required
def updateSetSize(request):
    PLAYLISTSIZE = SIZES.objects.all()[0].playlistSize
    if request.method == 'POST':
        newSetSize = int(request.POST.get('setSize'))
        if newSetSize<10 or newSetSize>3500 or newSetSize<PLAYLISTSIZE :
            mess = "Set Size should be >=10 and <=3500 and >=PlaylistSize"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            SETSIZE   = SIZES.objects.all()[0].setSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})
        else:
            siz = SIZES.objects.all()[0]
            siz.setSize=newSetSize
            siz.save()
            mess = "Set size Updated Succesfully"
            TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
            SETSIZE   = SIZES.objects.all()[0].setSize
            GAPSIZE      = SIZES.objects.all()[0].GapSize
            return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE,'mess':mess})

    else:
        TIMELIMITs = TIMELIMIT.objects.all()[0].timeLimit
        SETSIZE   = SIZES.objects.all()[0].setSize
        GAPSIZE      = SIZES.objects.all()[0].GapSize
        return render(request, 'users/settings.html',{'timeLimit':TIMELIMIT,'setSize':SETSIZE,'playlistSize':PLAYLISTSIZE,'gapSize':GAPSIZE})

