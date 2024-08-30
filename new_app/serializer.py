from .models import Tracket
from rest_framework.serializers import ModelSerializer

class TracketSerializer(ModelSerializer):
    class Meta:
        model = Tracket
        fields = "__all__"
