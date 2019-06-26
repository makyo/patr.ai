from django.contrib.auth.models import User
from django.db import models

from creators.models import Creator
from posts.models import Post


class Subscription(models.Model):

    patron = models.ForeignKey(User, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    amount = models.IntegerField()
    posts = models.ManyToManyField(Post)
