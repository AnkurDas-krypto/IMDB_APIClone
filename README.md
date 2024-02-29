# API Views

## WatchListAV

This view provides endpoints to list and create watchlists.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WatchList
from .serializers import WatchListSerializer


###WatchDetailAV
##This view provides endpoints to retrieve, update, and delete individual watchlists.

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

###WatchDetailAV
#This view provides endpoints to retrieve, update, and delete individual watchlists.

class WatchDetailAV(APIView):
    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response()

###StreamListAV
##This view provides endpoints to list and create stream platforms.

from .models import StreamPlatform
from .serializers import StreamPlatformSerializer

class StreamListAV(APIView):
    def get(self, request):
        stream = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

###StreamDetailAV
##This view provides endpoints to retrieve, update, and delete individual stream platforms.

class StreamDetailAV(APIView):
    def get(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    def put(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response()

###ReviewSerializer
##Serializer for the Review model.
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

###WatchListSerializer
##Serializer for the WatchList model.
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"

###StreamPlatformSerializer
##Serializer for the StreamPlatform model.
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
