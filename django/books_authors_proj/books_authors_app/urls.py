from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list),
    path('add_book' ,views.add_book),
    path('books/<int:book_id>', views.book),
    path('books/add_author',views.add_author_to_book),
    path('authors', views.authors_list),
    path('add_author',views.add_author),
    path('authors/<int:author_id>', views.author),
    path('authors/add_book', views.add_book_to_author),
]