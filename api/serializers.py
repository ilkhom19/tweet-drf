from rest_framework import serializers
from .models import Author,Tweet

class AuthorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['user_id','username','name']

class TweetSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
        'id',
        'conversation_id',
        'date',
        'time',
        'timezone',
        'auhtor',
        'tweet',
        'language',
        'replies_count',
        'retweets_count',
        'likes_count',
        'link',
        'retweet'
        ]