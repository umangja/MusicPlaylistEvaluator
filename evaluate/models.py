from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Songs(models.Model):
    songTitle = models.CharField(max_length=50)
    songAlbum = models.CharField(default = "Don't Know", max_length=50)
    songSinger= models.CharField(default = "Don't Know", max_length=50)
    link      = models.URLField(blank = False, max_length=200)

    def __str__(self):
        return str(self.id) 


class Algos(models.Model):
    algoName = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id) 


class Playlists(models.Model):
    playlistName = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return str(self.id)

class SongsInPlaylist(models.Model):
    playlistId = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    songId = models.ForeignKey(Songs, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) 

class Ratings(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    playlistId = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    algoId = models.ForeignKey(Algos, on_delete=models.CASCADE)

    R1 = models.IntegerField(default=-1)
    R2 = models.IntegerField(default=-1)
    R3 = models.IntegerField(default=-1)
    R4 = models.IntegerField(default=-1)
    R5 = models.IntegerField(default=-1)

    average1 = models.FloatField(default=-1)
    average2 = models.FloatField(default=-1)
    average3 = models.FloatField(default=-1)

    standardDeviation = models.FloatField(default=-1)
    variance          = models.FloatField(default=-1)

    distributionScore = models.FloatField(default=-1)
    correlationScore  = models.FloatField(default=-1)

    totalScore        = models.FloatField(default=-1)

    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.id) 



class Ordering(models.Model):
    ratingId = models.ForeignKey("Ratings", on_delete=models.CASCADE)
    songId   = models.ForeignKey("Songs" ,on_delete=models.CASCADE)
    position = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id)

