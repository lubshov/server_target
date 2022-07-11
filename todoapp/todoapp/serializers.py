from rest_framework import serializers
from .models import ListeningResponses


# Category serializer
class ListeningResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningResponses
        fields = '__all__'
