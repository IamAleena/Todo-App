from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('signup',views.Signup.as_view(), name='sign'),
    path('login',views.Login.as_view(), name='login'),
    path('signout',views.userlogout, name='signout'),
    path('action',views.Index.as_view())
    ]