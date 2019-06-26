from django.db import models

from creators.models import (
    Creator,
    Tier,
)


class Post(models.Model):

    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    body_rendered = models.TextField()
    min_tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    adult = models.BooleanField()


class Attachment(models.Model):

    DISPLAY_TYPES = (
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    display_type = models.CharField(max_length=5, choices=DISPLAY_TYPES)
    attachment = models.FileField()
