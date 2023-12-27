from django.db import models
from cloudinary.models import CloudinaryField
from apps.tags.models import Tag

# Create your models here.
class Home(models.Model):
    class Meta(object):
        db_table='home'
    tag= models.ForeignKey(
        Tag, on_delete=models.CASCADE, db_index=True
    )

    # price, rent_price, main_image, sub_image1,2,3,4, state, addresss, layout, created_at, updated_at
    price=models.FloatField(
        'price', blank=False,null=False, max_length=20, db_index=True
    )
    
    rent_price=models.FloatField(
        'price of rent', blank=False, null=False , max_length=20, db_index=True
    )

    main_image= CloudinaryField(
        'main image', blank=True, null=True
    )

    sub_image1= CloudinaryField(
        'sub image1', blank=True, null=True
    )

    sub_image2= CloudinaryField(
        'sub image2', blank=True, null=True
    )

    sub_image3= CloudinaryField(
        'sub image3', blank=True, null=True
    )

    sub_image4 = CloudinaryField(
        'sub image4', blank=True, null=True
    )
    state=models.CharField(
        'State',blank=False, null=False, max_length=30, db_index=True, default='State'
    )

    address=models.CharField(
        'Address', blank=False, null=False, max_length=100, db_index=True, default='address'

    )
    layout=models.CharField(
        'Layout', blank=True, null=True, max_length=50, default='bhk', db_index=True
    )

    created_at= models.DateTimeField(
        'Created Datetime',blank=True, auto_now_add=True
    )

    updated_at= models.DateTimeField(
       'lastly updated',blank=True, auto_now=True
    )





