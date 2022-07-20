from django.contrib import admin
from .models import Author, Tweet

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','username','user_id']
    pass

class TweetAdmin(admin.ModelAdmin):
    list_display = [
        'tweet',
        'date',
        'time',
        'user_id',
        'replies_count',
        'retweets_count',
        'likes_count',
        'link',
        'retweet'
        ]
    list_filter = ('user_id', 'date')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Tweet, TweetAdmin)