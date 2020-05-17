from django.urls import path
from .import views

urlpatterns = [
    path('shows',views.index),
    path('shows/new', views.new),
    path('shows/new/create',views.create),
    path('shows/<int:show_id>', views.show_info),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/edit/update', views.update),
    path('shows/<int:show_id>/destroy', views.destroy),
]