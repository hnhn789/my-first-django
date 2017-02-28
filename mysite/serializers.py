from rest_framework import serializers

from .models import Story


class StoryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('topic', 'content','points')