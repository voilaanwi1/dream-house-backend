from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import SellRequestSerializer
from .models import SellRequest
from .forms import SellRequestForm
from apps.users.mixins import CustomLoginRequiredMixin


# Create your views here.


class SellRequestAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = SellRequest.objects.all()
    serializer_class = SellRequestSerializer


    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id
        sellrequest_form = SellRequestForm(request.data)
        sellrequest = sellrequest_form.save()
        serializer = SellRequestSerializer([sellrequest], many = True)
        return Response(serializer.data[0])