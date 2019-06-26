from django.contrib.auth.models import User
from django.db import models


class Creator(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    about = models.TextField()
    

class Tier(models.Model):

    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    amount = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
