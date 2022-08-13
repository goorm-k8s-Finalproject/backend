from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from p2p.models import *
from p2p.serializers import *

# Create your views here.
class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.filter()
    serializer_class = AppSerializer

class AppDevViewSet(viewsets.ModelViewSet):
    queryset = AppDev.objects.filter()
    serializer_class = AppDevSerializer