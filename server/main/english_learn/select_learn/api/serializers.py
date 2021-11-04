from rest_framework import serializers
from select_learn.models import UserSentence, UserWord


class UserSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSentence
        fields = "__all__"


class UserWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWord
        fields = "__all__"
