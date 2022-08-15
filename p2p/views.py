from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action

from p2p.models import *
from p2p.serializers import *

# Create your views here.
class AppViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name']

class AppDevViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppDevSerializer
    queryset = AppDev.objects.all().order_by('app_dev_id')
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["app"]

class AppPubViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppPubSerializer
    queryset = AppPub.objects.all().order_by('app_pub_id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app"]

class AppGenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppGenreSerializer
    queryset = AppGenre.objects.all().order_by('genre')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app"]

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

class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["app"]