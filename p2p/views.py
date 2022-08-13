from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

import django_filters.rest_framework

from p2p.models import *
from p2p.serializers import *

# Create your views here.
class AppViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()

class AppDevViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppDevSerializer
    queryset = AppDev.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['app']
    def filter_queryset(self):
        app = self.kwargs['app']
        return AppDev.objects.filter(app=app)