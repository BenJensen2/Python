from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.users),
    path('new_user', views.new_user)
]