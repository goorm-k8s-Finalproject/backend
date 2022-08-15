from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from p2p.models import *
from p2p.serializers import *

# Create your views here.
# App
class AppViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["type"]
    search_fields = ['name']

class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app"]

class RecommendationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app"]

# DLC
class DLCViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DLCSerializer
    queryset = App.objects.all().order_by('app_id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["basegame"]

# Developer
class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all().order_by('developer_id')
    filter_backends = [SearchFilter]
    search_fields = ['name']

class AppDevViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppDevSerializer
    queryset = AppDev.objects.all().order_by('app_dev_id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app", "developer"]

# Publisher
class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all().order_by('publisher_id')
    filter_backends = [SearchFilter]
    search_fields = ['name']

class AppPubViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppPubSerializer
    queryset = AppPub.objects.all().order_by('app_pub_id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app", "publisher"]

# Genre
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('genre_id')
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['genre']
    filterset_fields = ["genre"]

class AppGenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppGenreSerializer
    queryset = AppGenre.objects.all().order_by('app_genre_id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app", "genre"]

# Price
class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all().order_by('-date')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["app"]
    search_fields = ['date']

# Store
class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StoreSerializer
    queryset = Price.objects.all().order_by('store_id')
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['store']
    filterset_fields = ["store"]