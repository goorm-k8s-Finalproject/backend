from rest_framework import serializers
from p2p.models import * # 모델 불러오기

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['app_id', 'name', 'header_url', 'release_date', 'type', "basegame_id"]

# Developer
class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ["developer_id", "name"]

class AppDevSerializer(serializers.HyperlinkedModelSerializer):
    developer = DeveloperSerializer(read_only = True)
    class Meta:
        model = AppDev
        fields = ["app_dev_id", "app", "developer"]

# Publisher
class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ["publisher_id", "name"]

class AppPubSerializer(serializers.HyperlinkedModelSerializer):
    publisher = PublisherSerializer(read_only = True)
    class Meta:
        model = AppPub
        fields = ["app_pub_id", "app", "publisher"]

# Genre
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre_id", "genre"]

class AppGenreSerializer(serializers.HyperlinkedModelSerializer):
    genre = GenreSerializer(read_only = True)
    class Meta:
        model = AppGenre
        fields = ["app_genre_id", "app", "genre"]

# Description
class DescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"

# Recommendation
class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"

# Price
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ["store_id", "store"]

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    store = StoreSerializer(read_only = True)
    class Meta:
        model = Price
        fields = "__all__"

# DLC
class DLCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['app_id', 'basegame']