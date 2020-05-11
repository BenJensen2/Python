from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

urlpatterns = [
    path('', views.index), # Creates home path to index function in views.py
]