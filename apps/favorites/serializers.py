from apps.users.serializers import UserSerializers

from .models import Favorite
from rest_framework import serializers


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class ListFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializers(many = False, read_only= True)

    class Meta:
        model = Favorite
        fields = '__all__'
        depth = 1