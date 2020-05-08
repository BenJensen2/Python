from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/DonkeyCheck', views.DonkeyCheck),
    path('/CurrentTime',views.time),
]