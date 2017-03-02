from rest_framework import serializers

from .models import Story, ItemList


class StoryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('title', 'content','points')

class SuccessSerializer(serializers.Serializer):
    success = serializers.BooleanField()