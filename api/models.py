from django.db import models

class Author(models.Model):

    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    conversation_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    timezone = models.CharField(max_length=70)
    user_id = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tweet = models.TextField(max_length=500)
    language =  models.CharField(max_length=70)
    replies_count = models.IntegerField()
    retweets_count = models.IntegerField()
    likes_count =  models.IntegerField()
    link = models.CharField(max_length=70)
    retweet = models.BooleanField()

    def __str__(self):
        return self.tweet

 


