from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create', views.create),
    path('login', views.login),
    path('success',views.success)
    # Do not allow user who is not logged in to reach /success
    # i.e. by making a GET request in the address bar
]