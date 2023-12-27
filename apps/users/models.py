from django.db import models

# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table = 'user'
    
    user_name = models.CharField(
        'User Name', blank= False, null=False, max_length=50, db_index=True
    )
    password = models.CharField(
        'password', blank = False, null = False,max_length=30, db_index= True
    )
    email = models.EmailField(
        'email', blank=False, null= False, max_length=100, db_index=True
    )
    token= models.CharField(
        'token', blank=True, null=True, max_length=500, db_index=True
    )
    token_expire_at=models.DateTimeField(
        'token expiry date', blank=True, null=True
    )
    created_at= models.DateTimeField(
        'Created Datetime',blank=True, auto_now_add=True
    )
    updated_at= models.DateTimeField(
       'lastly updated',blank=True, auto_now=True
    )

