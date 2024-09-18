from django.urls import path
from .views import AdvertListCreateView

urlpatterns = [
    path('adverts/', AdvertListCreateView.as_view(), name='advert-list-create'),
]
