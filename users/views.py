from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *
from evaluate.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
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
    ratings = Ratings.objects.filter(userId=current_user.id).order_by('-time')

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




