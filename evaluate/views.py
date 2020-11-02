from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
import random 
import numpy as np
from ShuflingAlgos.Fisher_Yates import *
from ShuflingAlgos.Fisher_yates_Repeated import *
from ShuflingAlgos.Elitist import *
from ShuflingAlgos.Elitist_Repeat import *
from .evaluationFunctions import *
from users.models import TIMELIMIT,SIZES
from MusicPlayer.constants import *
user = get_user_model()

songsName=["Go back to evalate page and start again"]
songsId=[-1]
songsAlbum=["Album"]
songsSinger=["Singer"]
songsLink=['Link']

@login_required
def evaluate(request):
    if request.method == 'POST':
        playlistId = request.POST['playlists']
        algoId     = int(request.POST['algos'])

        playlistName = Playlists.objects.get(id=int(playlistId)).playlistName
        algoName     = Algos.objects.get(id=algoId).algoName
        algoName = "Shuffling Algorithm - "+str(algoId)


        songsName.clear()
        songsId.clear()
        songsAlbum.clear()
        songsSinger.clear()
        songsLink.clear()

        
        SetSize = int(SIZES.objects.all()[0].setSize)
        playlistSize = int(SIZES.objects.all()[0].playlistSize)
        songs = Songs.objects.all().order_by('?')[:SetSize]

        tempSongIds=[]
        for song in songs:
            curSongId=song.id
            tempSongIds.append(curSongId)

        if algoId == 2:
           tempSongIds=Fisher_yates(tempSongIds)
        elif algoId == 1:
            tempSongIds=Etilist_Shuffle(tempSongIds)
        elif algoId == 4:
            tempSongIds=Fisher_yates_Repeated(tempSongIds,SetSize,10)
        elif algoId == 3:
            tempSongIds=Etilist_Shuffle_repeated(tempSongIds,5,SetSize,10)
            

        tempSongIds = tempSongIds[:playlistSize]

        for id in tempSongIds:
            singleSong = Songs.objects.filter(id=id)

            curSongName=singleSong[0].songTitle
            curSongId=singleSong[0].id
            curSongAlbum=singleSong[0].songAlbum
            curSongSinger=singleSong[0].songSinger
            curSongLink=singleSong[0].link
            
            songsName.append(curSongName)
            songsId.append(curSongId)
            songsAlbum.append(curSongAlbum)
            songsSinger.append(curSongSinger)
            songsLink.append(curSongLink)

        timeLimit = int(TIMELIMIT.objects.all()[0].timeLimit)
        gapSize  =  int(SIZES.objects.all()[0].GapSize)

        return render(request, 'evaluate/printSongsList.html',{'songs':songs,'songsAlbum':songsAlbum,'songsSinger':songsSinger,'songsLink':songsLink ,'playlistId':playlistId,'playlistName':playlistName,'algoName':algoName,'algoId':algoId,'songsName':songsName,'songsId':songsId,'timeLimit':timeLimit,'gapSize':gapSize,'infos':INFORMATION_ABOVE_SONG_LIST,'ratingMeanings':RATINGS_MEANING })

    else:
        playlists = Playlists.objects.all()
        algos     = Algos.objects.all()
        return render(request, 'evaluate/selectPlaylistAndAlgo.html',{'playlists':playlists,'algos':algos})

@login_required
def saveRatings(request):
    if request.method == 'POST':

        rating1 = request.POST.get('rating1.0',0)
        rating2 = request.POST.get('rating2.0',0)
        rating3 = request.POST.get('rating3.0',0)
        rating4 = request.POST.get('rating4.0',0)
        rating5 = request.POST.get('rating5.0',0)


        rating6 = request.POST.get('rating6.0',0)
        rating7 = request.POST.get('rating7.0',0)
        rating8 = request.POST.get('rating8.0',0)
        rating9 = request.POST.get('rating9.0',0)
        rating10 = request.POST.get('rating10.0',0)

        playlistId = request.POST['playlistId']
        algoId     = request.POST['algoId']

        playlistName = Playlists.objects.get(id=int(playlistId)).playlistName
        algoName     = Algos.objects.get(id=int(algoId)).algoName

        playlist = Playlists.objects.get(id=playlistId)
        algo     = Algos.objects.get(id=algoId)
        current_user = request.user

        if len(songsName)==0 or songsName[0]=="Go back to evalate page and start again" :
            return redirect('/')         
        
        
        ratinglist = [int(rating1),int(rating2),int(rating3), int(rating4), int(rating5),int(rating6),int(rating7),int(rating8),int(rating9),int(rating10) ]

        normalAverage = findNormalAverage(ratinglist)
        WeightedAverage1 = findWeightedAverage1(ratinglist)
        WeightedAverage2 = findWeightedAverage2(ratinglist)
        std              = findStandardDeviationAndVariance(ratinglist)['std']
        var              = findStandardDeviationAndVariance(ratinglist)['var']
        DistributionScore = findDistributionScore(songsId) 
        CorrelationScore = findCorrelationScore(ratinglist)
        totalScore       = findTotalScore(normalAverage,DistributionScore)
        

        ratingId  = Ratings(playlistId=playlist,userId=current_user,algoId=algo, R1=rating1, R2=rating2, R3=rating3, R4=rating4, R5=rating5, R6=rating6, R7=rating7, R8=rating8, R9=rating9, R10=rating10 ,average1=normalAverage,average2=WeightedAverage1,average3=WeightedAverage2,variance=var,standardDeviation=std,distributionScore=DistributionScore,correlationScore=CorrelationScore,totalScore=totalScore)
        rating =  Ratings.objects.none()

        ratingId.save()

        request.session['ratingId'] = ratingId.id
        rating = Ratings.objects.get(id=ratingId.id)

        pos = 1
        for songId in songsId:
            song = Songs.objects.get(id=songId)
            order = Ordering(songId=song,ratingId=rating,position=pos)
            order.save()
            pos=pos+1
        return redirect('/showSummary')
    else:
        return redirect('/')



@login_required
def showSummary(request):
    rating   = Ratings.objects.get(id=int(request.session['ratingId']))
    ordering = Ordering.objects.filter(ratingId=rating).order_by('position')
    gapSize  =  int(SIZES.objects.all()[0].GapSize)
    return render(request,'evaluate/showSummary.html',{'rating':rating,'ordering':ordering,'gapSize':gapSize})

