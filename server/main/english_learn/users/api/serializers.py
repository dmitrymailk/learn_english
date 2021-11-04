from rest_framework import serializers
from users.models import CustomUser
from users.models import UserMeta


from django.db.models.signals import post_save
from django.dispatch import receiver

# from users.api.serializers import UserMetaSerializer
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username']


class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMeta
        # exclude = ['user']
        fields = "__all__"


@receiver(post_save, sender=CustomUser)
def add_score(sender, instance, created, **kwargs):

    if created:
        # print("CREATED", vars(sender), sender.id, vars(instance), instance.id)
        user_id = instance
        new_usermeta = {"user_id": instance, }
        serializer = UserMetaSerializer(data=new_usermeta)
        if serializer.is_valid():
            serializer.save()
            # print("Saved")
        else:
            print("UserMetaSerializer", serializer.errors)
