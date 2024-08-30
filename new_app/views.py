from django.shortcuts import render
from .models import Tracket
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import TracketSerializer

class TacketDisplay(ListCreateAPIView):
    queryset = Tracket.objects.all()
    serializer_class = TracketSerializer

class TracketModifier(RetrieveUpdateDestroyAPIView):
    queryset = Tracket.objects.all()
    serializer_class = TracketSerializer   

