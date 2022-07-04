from django.db import models

class Author(models.Model):

    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=70)

class Tweet(models.Model):
    id = models.IntegerField()
    conversation_id = models.IntegerField()
    created_at = models.CharField()
    date = models.DateField()
    time = models.TimeField()
    timezone = models.CharField()
    auhtor = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tweet = models.TextField(max_length=500)
    language =  models.CharField()
    replies_count = models.IntegerField()
    retweets_count = models.IntegerField()
    likes_count =  models.IntegerField()
    link = models.CharField()
    retweet = models.BooleanField()
 


