from django.urls import path
from .views import  SignUp, Activation

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('activation', Activation, name='activation'),
]