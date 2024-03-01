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



### Usig Mixins

## ReviewList

This view provides endpoints to list and create reviews.

```python
from rest_framework import generics, mixins
from .models import Review
from .serializers import ReviewSerializer

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

##ReviewDetail
#This view provides endpoints to retrieve individual reviews.

python
Copy code
class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


## Generics

### ReviewCreate

This view allows users to create reviews for watchlist items. It extends `generics.CreateAPIView` and requires a valid `ReviewSerializer` for creating reviews. It includes custom logic to prevent users from creating multiple reviews for the same watchlist item.

- **HTTP Methods:**
  - `POST`: Creates a new review for the specified watchlist item.
  
- **Attributes:**
  - `serializer_class`: Specifies the serializer class used for review creation.

- **Methods:**
  - `get_queryset`: Returns all existing reviews.
  - `perform_create`: Overrides the default create behavior to associate the review with the appropriate watchlist item and user. It also checks if the user has already reviewed the item to prevent duplicate reviews.


```python 
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You already have a review")

        serializer.save(watchlist=watchlist, review_user=review_user)


perform_create function checks if the same user is reviewing twice. 

### ReviewList

This view lists reviews associated with a specific watchlist item. It extends `generics.ListCreateAPIView` and requires a valid `ReviewSerializer` for serialization.

- **HTTP Methods:**
  - `GET`: Retrieves a list of reviews associated with the specified watchlist item.
  - `POST`: Creates a new review for the specified watchlist item.

- **Attributes:**
  - `serializer_class`: Specifies the serializer class used for serialization.

- **Methods:**
  - `get_queryset`: Returns all reviews associated with the specified watchlist item.


```python
class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer  

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

### ReviewDetail

This view provides detailed information about a specific review. It extends `generics.RetrieveUpdateDestroyAPIView` and requires a valid `ReviewSerializer` for serialization.

```python
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

- **HTTP Methods:**
  - `GET`: Retrieves detailed information about the specified review.
  - `PUT`: Updates the specified review.
  - `DELETE`: Deletes the specified review.

- **Attributes:**
  - `queryset`: Specifies the queryset used to retrieve reviews.
  - `serializer_class`: Specifies the serializer class used for serialization.

```python
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  


