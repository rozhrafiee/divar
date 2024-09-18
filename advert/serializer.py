
from rest_framework import serializers
from .models import Advert

class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'price', 'capacity', 'source', 'destination', 'category', 'user', 'created_at', 'updated_at']
