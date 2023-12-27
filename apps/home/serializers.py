from .models import Home
from rest_framework import serializers

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model= Home
        field = "__all__"