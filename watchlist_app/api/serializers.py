from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review



"""
Model Serializer 
"""
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

    # def validate_name(self, value):
    #      if len(value) < 3:
    #          raise serializers.ValidationError("name is too short")
    #      return value


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many = True, read_only = True)
    """ 
    for using hyperlink on stream platforms
    """
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = 'movie-details'
    # )
    class Meta:
        model = StreamPlatform
        fields = "__all__"






# def name_length(value):
#     if len(value) < 3:
#             raise serializers.ValidationError("name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()


#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance 

#     """
#     field level validation
#     """
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError("name is too short")
#     #     return value
    
#     """
#     Validators: use as a function parameter
#     """