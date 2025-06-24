from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    count_likes = models.IntegerField(default=0)
    count_comment = models.IntegerField(default=0)
    count_retweet = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tweet by {self.user.username} ({self.created_at.date()}): "{self.text[:30]}..."'