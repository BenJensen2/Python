from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager, Book, BookManager, Author, AuthorManager, Review, ReviewManager
from django.contrib import messages

def index(request):
    if 'user_email' in request.session:
    
        context = {
            'first_name' : request.session['fname']# User.objects.get(email_address=request.session['user_email']).first_name
        }
        return render(request,'books.html',context)
    else:
        return HttpResponse('You do not have access to this site.  Login to proceed')

def add(request):
    if 'user_email' not in request.session:
        return HttpResponse('You do not have access to this site.  Login to proceed')
    context = {
        'all_authors' : Author.objects.all()
    }

    return render(request,'book_add.html',context)

def book_info(request,book_id):
    # context = {
    #     'book' : books.objects.get(id=book_id),
    #     'authors': books.objects.get(id=book_id).authors_included.all(),
    #     'all_authors' : authors.objects.all()
    # }
    # print(context)
    return render(request,'book_info.html')

def create(request):

    book_errors = Book.objects.book_validator(request.POST)

    if len(book_errors) > 0:
        for key, value in book_errors.items():
            messages.error(request,value,extra_tags=key)

        author_errors = Author.objects.author_validator(request.POST)

        if len(author_errors) > 0:
            for key, value in author_errors.items():
                messages.error(request,value,extra_tags=key)
            
            review_errors = Review.objects.review_validator(request.POST)
            
            if len(review_errors) > 0:
                for key, value in review_errors.items():
                    messages.error(request,value,extra_tags=key)
                
                # New Book
                title = request.POST['book_title']
                book = Book.objects.create(title=title)


    # if 'author_added' in request.POST:
    #     author1 = Author.objects.get(id=request.POST['author_added'])
    # if 'new_author' in request.POST:
    #     author2 = Author.objects.create(name=request.POST['new_author'])

    # if author1:
    #     book.authors_included.add(author1)
    # if author2:
    #     book.authors_included.add(author2)

    # if 'review' in request.POST:
    #     user = User.objects.get(email_address = request.session['user_email'])
    #     review = Review.objects.create(text=request.POST['new_review'],
    #     rating=request.POST['rating'])
    #     review.book.add(book)
    #     review.user.add(user)

        book_id = book.id
        return redirect(f'/books/add')