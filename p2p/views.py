from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import SearchFilter

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
    queryset = AppDev.objects.all()
    filter_backends = [DjangoFilterBackend]