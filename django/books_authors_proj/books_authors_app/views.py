from django.shortcuts import render, HttpResponse, redirect
from .models import *

# def index(request):
#     return HttpResponse('This Works!!')

def books_list(request):
    context = {
        'all_books' : books.objects.all()
    }
    return render(request,'books_list.html',context)

def add_book(request):
    print('book added')
    book_title = request.POST['title']
    description = request.POST['desc']
    books.objects.create(title = book_title, desc = description)
    return redirect('../')

def book(request,book_id):
    context = {
        'book' : books.objects.get(id=book_id),
        'authors': books.objects.get(id=book_id).authors_included.all(),
        'all_authors' : authors.objects.all()
    }
    print(context)
    return render(request,'book.html',context) # HttpResponse(f'This is book number {book_id}')

def add_author_to_book(request):
    print('author added to book')
    author_added = request.POST['author_added']
    book_id = request.POST['book_id']
    book = books.objects.get(id=book_id)
    author = authors.objects.get(id=author_added)
    book.authors_included.add(author)
    return redirect('../')
    # Jane Austen added twice, in db as well? No, only adds once

def authors_list(request):
    context = {
        'all_authors' : authors.objects.all()
    }

    return render(request,'authors_list.html',context)

def add_author(request):
    print('New Author Added');
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    authors.objects.create(first_name = first_name, last_name = last_name, notes = notes)
    return redirect('../authors')

def author(request,author_id):
    context = {
        'author' : authors.objects.get(id=author_id),
        'books': authors.objects.get(id=author_id).authored_books.all(),
        'all_books' : books.objects.all()
    }
    print(context)
    return render(request,'author.html',context)

def add_book_to_author(request):
    print('book added to author')
    book_added = request.POST['book_added']
    author_id = request.POST['author_id']
    book = books.objects.get(id=book_added)
    author = authors.objects.get(id=author_id)
    author.authored_books.add(book)
    return redirect('../')
