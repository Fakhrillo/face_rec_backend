from rest_framework import serializers
from .models import UserInfo, Photos_to_check


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class Photos_to_check(serializers.ModelSerializer):
    class Meta:
        model = Photos_to_check
        fields = '__all__'
