from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from apps.users.mixins import CustomLoginRequiredMixin
from .models import Favorite, Home
from .serializers import FavoriteSerializer, ListFavoriteSerializer

# Create your views here.

class FavoriteList(CustomLoginRequiredMixin, generics.ListAPIView):
    serializer_class = ListFavoriteSerializer


    def get(self, request, *args, **kwargs):
        self.queryset = Favorite.objects.order_by('-created_at').filter(user_id = request.login_user.id)
        return self.list(request, *args, **kwargs)
    


class FavoriteAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = ListFavoriteSerializer

    def post(self, request, *args, **kwargs):
        serializer = FavoriteSerializer()
        serializer.validate(request.data)
        home_id = int(request.data['home'])
        print("home", home_id)
        home = Home.objects.get(id=home_id)

        existed = Favorite.objects.filter(home=home_id, user = request.login_user.id).first()
        print("existed", existed)

        if existed is not None:
            return Response('Home is already saved', status.HTTP_400_BAD_REQUEST)
        if(home is None):
            return Response('Home not found.', status.HTTP_400_BAD_REQUEST)
        
        request.data['user'] = request.login_user.id
        request.data['home'] = home.id

        return self.create(request, *args, **kwargs)




class FavoriteDelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'id'
    

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['id']
        favorite = Favorite.objects.filter(user_id= request.login_user.id, id=id).first()

        if favorite is None:
            return Response('Favorite not found.', status.HTTP_400_BAD_REQUEST)
        self.destroy(request, *args, **kwargs)

        return Response({'message': "Success."})