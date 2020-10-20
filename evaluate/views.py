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
from users.models import TIMELIMIT
user = get_user_model()

songsName=["Go back to evalate page and start again"]
songsId=[-1]
songsAlbum=["Album"]
songsSinger=["Singer"]
songsLink=['Link']

# def home(request):  
#     if request.user.is_authenticated:
#         return render(request, 'users/profile.html')
#     else:
#         context = { 'posts': Post.objects.all() }
#         return render(request, 'blog/home.html', context)


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})





@login_required
def evaluate(request):
    if request.method == 'POST':
        playlistId = request.POST['playlists']
        algoId     = int(request.POST['algos'])

        playlistName = Playlists.objects.get(id=int(playlistId)).playlistName
        algoName     = Algos.objects.get(id=algoId).algoName

        # songs = Songs.objects.all()
        # print(songs)
        # print(songs[1].songSinger)


        songsName.clear()
        songsId.clear()
        songsAlbum.clear()
        songsSinger.clear()
        songsLink.clear()

        songIds = SongsInPlaylist.objects.select_related().filter(playlistId=playlistId)
        songs = Songs.objects.none()
        for song in songIds:
            songIdInt = str(song.songId)
            singleSong = Songs.objects.filter(id=int(songIdInt))
            songs|=singleSong

        tempSongIds=[]
        for song in songs:
            curSongId=song.id
            tempSongIds.append(curSongId)

        print(tempSongIds)

        if algoId == 2:
           tempSongIds=Fisher_yates(tempSongIds)
        elif algoId == 1:
            tempSongIds=Etilist_Shuffle(tempSongIds)
        elif algoId == 4:
            tempSongIds=Fisher_yates_Repeated(tempSongIds)
        elif algoId == 3:
            tempSongIds=Etilist_Shuffle_repeated(tempSongIds)
            

        print(tempSongIds)

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

        print(songs)
        print(songsName)
        print(songsId)
        timeLimit = int(TIMELIMIT.objects.all()[0].timeLimit)
        return render(request, 'evaluate/printSongsList.html',{'songs':songs,'songsAlbum':songsAlbum,'songsSinger':songsSinger,'songsLink':songsLink ,'playlistId':playlistId,'playlistName':playlistName,'algoName':algoName,'algoId':algoId,'songsName':songsName,'songsId':songsId,'timeLimit':timeLimit })

    else:
        playlists = Playlists.objects.all()
        algos     = Algos.objects.all()
        return render(request, 'evaluate/selectPlaylistAndAlgo.html',{'playlists':playlists,'algos':algos})

@login_required
def saveAndShowSummary(request):
    if request.method == 'POST':

        rating1 = request.POST.get('rating1.0',0)
        rating2 = request.POST.get('rating2.0',0)
        rating3 = request.POST.get('rating3.0',0)
        rating4 = request.POST.get('rating4.0',0)
        rating5 = request.POST.get('rating5.0',0)

        playlistId = request.POST['playlistId']
        algoId     = request.POST['algoId']

        playlistName = Playlists.objects.get(id=int(playlistId)).playlistName
        algoName     = Algos.objects.get(id=int(algoId)).algoName

        playlist = Playlists.objects.get(id=playlistId)
        algo     = Algos.objects.get(id=algoId)
        current_user = request.user

        # songs = Songs.objects.none()
        # for id in songsId:
        #     singleSong = Songs.objects.filter(id=id)
        #     songs|=singleSong

        # songs = request.POST['songs']
        # songsName = request.POST['songsName']
        # songsId = request.POST['songsId']

        # songsName = request.session.get('songsName')

        print(rating1)
        print(rating2)
        print(rating3)
        print(rating4)
        print(rating5)
        print(current_user.id)
        print(current_user.username)
        print(songsName)
        print(songsId)

        if len(songsName)==0 or songsName[0]=="Go back to evalate page and start again" :
            return redirect('/')         
        
        
        ratinglist = [int(rating1),int(rating2),int(rating3), int(rating4), int(rating5)]
        print(ratinglist)
        normalAverage = findNormalAverage(ratinglist)
        WeightedAverage1 = findWeightedAverage1(ratinglist)
        WeightedAverage2 = findWeightedAverage2(ratinglist)
        std              = findStandardDeviationAndVariance(ratinglist)['std']
        var              = findStandardDeviationAndVariance(ratinglist)['var']
        DistributionScore = findDistributionScore(ratinglist) 
        CorrelationScore = findCorrelationScore(ratinglist)
        totalScore       = findTotalScore(normalAverage,DistributionScore)
        

        ratingId  = Ratings(playlistId=playlist,userId=current_user,algoId=algo, R1=rating1, R2=rating2, R3=rating3, R4=rating4, R5=rating5,average1=normalAverage,average2=WeightedAverage1,average3=WeightedAverage2,variance=var,standardDeviation=std,distributionScore=DistributionScore,correlationScore=CorrelationScore,totalScore=totalScore)
        rating =  Ratings.objects.none()
        if not Ratings.objects.filter(playlistId=playlist,userId=current_user,algoId=algo, R1=rating1, R2=rating2, R3=rating3, R4=rating4, R5=rating5,average1=normalAverage,average2=WeightedAverage1,average3=WeightedAverage2,variance=var,standardDeviation=std,distributionScore=DistributionScore,correlationScore=CorrelationScore,totalScore=totalScore).exists():
            ratingId.save()
            rating = Ratings.objects.get(id=ratingId.id)
        else:
            rating = Ratings.objects.filter(playlistId=playlist,userId=current_user,algoId=algo, R1=rating1, R2=rating2, R3=rating3, R4=rating4, R5=rating5,average1=normalAverage,average2=WeightedAverage1,average3=WeightedAverage2,variance=var,standardDeviation=std,distributionScore=DistributionScore,correlationScore=CorrelationScore,totalScore=totalScore)[0]

        print(rating.R1)

        # return render(request,'evaluate/showSummary.html',{'rating':rating,'songs':songs,'songsName':songsName,'songsId':songsId})
        return render(request,'evaluate/showSummary.html',{'rating':rating,'songsAlbum':songsAlbum,'songsSinger':songsSinger,'songsLink':songsLink ,'playlistId':playlistId,'playlistName':playlistName,'algoName':algoName, 'algoId':algoId,'songsName':songsName,'songsId':songsId, 'algoName': algo.algoName , 'playlistName': playlist.playlistName,
                                                           'normalAverage' : normalAverage,
                                                           'WeightedAverage1':WeightedAverage1,
                                                           'WeightedAverage2':WeightedAverage2,
                                                           'std':std,
                                                           'var':var,
                                                           'DistributionScore':DistributionScore,
                                                           'CorrelationScore':CorrelationScore,
                                                           'totalScore':totalScore})

    else:
        return redirect('/')
