from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TIMELIMIT(models.Model):
    timeLimit =models.IntegerField(null=False,default=10)
    def __str__(self):
        return str(self.timeLimit)
