from django.db import models
from apps.users.models import User


# Create your models here.

class SellRequest(models.Model):
    class Meta(object):
        db_table='sellrequest'
    user=models.ForeignKey(
        User,on_delete=models.CASCADE
    )
    address=models.CharField(
        'Address', blank=False, null=False, max_length=100, db_index=True, default='address'

    )
    sqft=models.CharField(
        'SQFT', blank=False, null= False, max_length=60, db_index=True, default='sqft'
    )
    age_building=models.IntegerField(
        'age of building', blank=False, null=False, db_index=True
    )
    created_at=models.DateTimeField(
        'created date time', blank=True, auto_now_add=True
    )
    updated_at=models.DateTimeField(
        'updated date time', blank=True, auto_now=True
    )





