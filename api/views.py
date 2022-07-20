from django.shortcuts import render
from rest_framework.response import Response
from .serializers import AuthorSerializer, TweetSerializer, FileUploadSerializer
from .models import Author, Tweet
from rest_framework.decorators import api_view
from rest_framework import status ,generics
import io, csv, pandas as pd

@api_view(['GET', 'POST'])
def author_list(request):

    if request.method == 'GET':
        authors  = Author.objects.all()
        serializer = AuthorSerializer(authors, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def tweet_list(request):

    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = AuthorSerializer(tweets, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TweetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthorUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Author(
                       user_id = row['user_id'],
                       username = row["username"],
                       name = row['name']
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class TweetUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Tweet(
                       id = row['id'],
                       conversation_id = row['conversation_id'],
                       date = row['date'],
                       time = row['time'],
                       timezone = row['timezone'],
                       user_id = Author.objects.get(user_id = row['user_id']),
                       tweet = row['tweet'],
                       language = row['language'],
                       replies_count = row['replies_count'],
                       retweets_count = row['retweets_count'],
                       likes_count = row['likes_count'],
                       link = row['link'],
                       retweet = row['retweet']
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)