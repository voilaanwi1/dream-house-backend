from django.shortcuts import render
from rest_framework import generics
from .serializers import TagSerializers
from .models import Tag

# Create your views here.


class TagList(generics.ListAPIView):
    queryset=Tag.objects.order_by('-created_at').all()
    serializer_class=TagSerializers

class TagAdd(generics.CreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializers

class TagDetail(generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializers

class TagDelete(generics.DestroyAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializers

