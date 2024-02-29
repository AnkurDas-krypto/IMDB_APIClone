
### APIView views.py

- class WatchListAV(APIView):
        def get(self, request):
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies, many = True)
            return Response(serializer.data)
        
        def post(self, request):
            serializer = WatchListSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)



- class WatchDetailAV(APIView):
        def get(self, request, pk):
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)

        def put(self, request, pk):
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        def delete(self, request, pk):
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response()


- class StreamListAV(APIView):
        def get(self, request):
            stream = StreamPlatform.objects.all()
            # for using hyperlink on serializer we use context
            #serializer = StreamPlatformSerializer(stream, many = True, context = {'request': request})
            serializer = StreamPlatformSerializer(stream, many = True)
            return Response(serializer.data)

        def post(self, request):
            serializer = StreamPlatformSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        
- class StreamDetailAV(APIView):
        def get(self, request, pk):
            stream = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(stream)
            return Response(serializer.data)
        def put(self, request, pk):
            stream = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(stream, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
            
        def delete(self, request, pk):
            stream = StreamPlatform.objects.get(pk=pk)
            stream.delete()
            return Response()


### serializers.py


- class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = "__all__"

- class WatchListSerializer(serializers.ModelSerializer):
        reviews = ReviewSerializer(many=True, read_only=True)
        class Meta:
            model = WatchList
            fields = "__all__"




- class StreamPlatformSerializer(serializers.ModelSerializer):

        watchlist = WatchListSerializer(many = True, read_only = True)
        class Meta:
            model = StreamPlatform
            fields = "__all__"

