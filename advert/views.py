# advert/views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView

from .models import Advert
from .serializer import AdvertSerializer

class AdvertListCreateView(ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]  
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["price", "capacity"]
    search_fields = ["title"]
    filterset_fields = ['source', 'destination']

    def perform_create(self, serializer):
        # Automatically assign the authenticated user to the created advert
        serializer.save(user=self.request.user)
