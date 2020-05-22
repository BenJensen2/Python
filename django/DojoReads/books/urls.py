from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/add', views.add),
    path('/add/create',views.create),
    path('/<int:book_id>', views.book_info),
]