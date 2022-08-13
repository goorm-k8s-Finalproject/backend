from rest_framework import serializers

from p2p.models import * # 모델 불러오기

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ['app_id', 'name', 'header_url', 'release_date', 'type']

class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ["developer_id", "name"]

class AppDevSerializer(serializers.HyperlinkedModelSerializer):
    developer = DeveloperSerializer(read_only = True)
    class Meta:
        model = AppDev
        fields = ["app", "developer"]