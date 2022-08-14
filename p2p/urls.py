from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from p2p import views


router = routers.DefaultRouter()

router.register(r'app', views.AppViewSet, basename = "app")
router.register(r'appdev', views.AppDevViewSet, basename = "appdev")

urlpatterns = [
    path('', include(router.urls)),
]