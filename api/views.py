from django.shortcuts import render
from rest_framework.response import Response
from .serializers import AuthorSerializer, TweetSerializer
from .models import Author, Tweet
from rest_framework.decorators import api_view
from rest_framework import status


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