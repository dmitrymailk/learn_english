from rest_framework import serializers
from .models import UserWords, TedWords, UserWordsTask2, UserWordsTaskUser


class UserWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWords
        fields = "__all__"


class TedWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TedWords
        fields = "__all__"


class UserWordsTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWordsTask2
        fields = "__all__"


class UserWordsTaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWordsTaskUser
        fields = "__all__"
