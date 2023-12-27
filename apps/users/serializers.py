from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password,check_password
from secrets import token_hex
import datetime

class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('user_name', 'password', 'email', 'token', 'token_expire_at')

class UserSignUpSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only = True)
    token=serializers.CharField(read_only= True)
    token_expire_at=serializers.DateTimeField(read_only=True)
    class Meta:
        model=User
        fields=('user_name','password', 'email', 'token', 'token_expire_at')

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        validated_data['token']= token_hex(30)
        validated_data['token_expire_at']=datetime.datetime.now() + datetime.timedelta(days=7)

        return super().create(validated_data)

class UserSignInSerializers(serializers.ModelSerializer):
    user_name= serializers.CharField(read_only = True)
    password=serializers.CharField(write_only = True)
    email=serializers.EmailField()
    token=serializers.CharField(read_only = True)
    token_expire_at=serializers.DateTimeField(read_only=True)
    class Meta:
        model=User
        fields=('user_name','password', 'email','token','token_expire_at')

    def create(self, validated_data):
        user=User.objects.filter(email=validated_data['email'])
        if len(user)>0 and check_password(validated_data['password'],user[0].password):
            user[0].token = token_hex(30)
            user[0].token_expire_at=datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save()

            return user[0]
        else:
            raise serializers.ValidationError({"error":"The password or email is incorrect"})
    