from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from p2p import views


router = routers.DefaultRouter()

router.register(r'app', views.AppViewSet, basename = "app")
router.register(r'appdev', views.AppDevViewSet, basename = "appdev")
router.register(r'apppub', views.AppPubViewSet, basename = "apppub")
router.register(r'appgenre', views.AppGenreViewSet, basename = "appgenre")
router.register(r'description', views.DescriptionViewSet, basename = "description")
router.register(r'recommendation', views.RecommendationViewSet, basename = "recommendation")
router.register(r'price', views.PriceViewSet, basename = "price")
router.register(r'dlc', views.DLCViewSet, basename = "dlc")
router.register(r'developer', views.DeveloperViewSet, basename = "developer")
router.register(r'publisher', views.PublisherViewSet, basename = "publisher")
router.register(r'genre', views.GenreViewSet, basename = "genre")
router.register(r'store', views.StoreViewSet, basename = "store")

urlpatterns = [
    path('', include(router.urls)),
]