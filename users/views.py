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

    print(ratings)
    print(playlistNames)
    print(algoNames)


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

        print(ratings)
        print(playlistNames)
        print(algoNames)


        return render(request,'users/showAllRatingWithTimming.html',{'ratings':ratings, 'playlistNames':playlistNames, 'algoNames':algoNames,})
    else:
        TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
        return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT})

@login_required
def updateTimeLimit(request):
    if request.method == 'POST':
        newTimeLimit = int(request.POST.get('timeLimit'))
        if newTimeLimit<5 or newTimeLimit>300 :
            mess = "Time Limit should be >=5 and <=300"
            TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
            allUsers   = user.objects.all(); 
            return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'mess':mess,'allUsers':allUsers})
        else:
            TIME_LIMIT=newTimeLimit
            timelimit = TIMELIMIT.objects.all()[0]
            timelimit.timeLimit=newTimeLimit
            timelimit.save()
            mess = "Time Limit Updated Succesfully"
            allUsers   = user.objects.all(); 
            return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'mess':mess,'allUsers':allUsers})

    else:
        TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
        allUsers   = user.objects.all(); 
        return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'allUsers':allUsers})



# @login_required
# def updateSetSize(request):
#     if request.method == 'POST':
#         newTimeLimit = int(request.POST.get('setsize'))
#         if newTimeLimit<5 or newTimeLimit>300 :
#             mess = "Time Limit should be >=5 and <=300"
#             TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
#             allUsers   = user.objects.all(); 
#             return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'mess':mess,'allUsers':allUsers})
#         else:
#             TIME_LIMIT=newTimeLimit
#             timelimit = TIMELIMIT.objects.all()[0]
#             timelimit.timeLimit=newTimeLimit
#             timelimit.save()
#             mess = "Time Limit Updated Succesfully"
#             allUsers   = user.objects.all(); 
#             return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'mess':mess,'allUsers':allUsers})

#     else:
#         TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)
#         allUsers   = user.objects.all(); 
#         return render(request, 'users/profile.html',{'timeLimit':TIME_LIMIT,'allUsers':allUsers})

