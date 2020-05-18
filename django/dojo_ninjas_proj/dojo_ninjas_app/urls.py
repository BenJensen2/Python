from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ninjas', views.all_ninjas),
    path('new_dojo', views.new_dojo),
    path('new_ninja', views.new_ninja),
    path('delete_dojo', views.delete_dojo),
    path('delete_ninja', views.delete_ninja),
]