from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from p2p import views


router = routers.DefaultRouter()

router.register(r'app', views.AppViewSet, basename = "app")
router.register(r'appdev', views.AppDevViewSet, basename = "appdev")
router.register(r'apppub', views.AppPubViewSet, basename = "apppub")
router.register(r'appgenre', views.AppGenreViewSet, basename = "appgenre")

urlpatterns = [
    path('', include(router.urls)),
]