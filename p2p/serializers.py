from rest_framework import serializers
from p2p.models import * # 모델 불러오기

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['app_id', 'name', 'header_url', 'release_date', 'type']

# Developer
class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ["developer_id", "name"]

class AppDevSerializer(serializers.HyperlinkedModelSerializer):
    developer = DeveloperSerializer(read_only = True)
    #app = AppSerializer(read_only = True)
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
