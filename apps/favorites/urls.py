from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavoriteList.as_view(), name='favorite_list'),
    path('add/', views.FavoriteAdd.as_view(), name='favorite_add'),
    path('delete/<int:id>', views.FavoriteDelete.as_view(), name='favorite_delete'),
]