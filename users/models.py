from django.db import models

class TIMELIMIT(models.Model):
    timeLimit =models.IntegerField(null=False,default=10)
    def __str__(self):
        return str(self.timeLimit)

class SIZES(models.Model):
    setSize = models.IntegerField(null=False,default=1000)
    playlistSize = models.IntegerField(null=False,default=50)
    def __str(self):
        return str(self.id)