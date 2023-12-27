from django.urls import path
from . import views

urlpatterns=[
    path('',views.UserList.as_view(),name='user_list'),
    path('signin/',views.UserSignIn.as_view(),name='user_sign_in'),
    path('signup/',views.UserSignUp.as_view(),name='user sign up'),
    path('check-login/',views.UserCheckLogin.as_view(),name='user check login')
]