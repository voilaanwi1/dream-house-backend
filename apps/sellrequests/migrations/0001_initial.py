# Generated by Django 5.0.2 on 2024-02-21 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, default='Address', max_length=100, verbose_name='Address')),
                ('sqft', models.CharField(db_index=True, default='SQFT', max_length=50, verbose_name='SQFT')),
                ('age_building', models.IntegerField(db_index=True, verbose_name='Age of Building')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'sellrequest',
            },
        ),
    ]
