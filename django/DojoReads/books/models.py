from django.db import models
from users.models import User, UserManager


class BookManager(models.Manager):
    def book_validator(self,postData):
        errors = {}

        book = Book.objects.filter(title=postData['book_title'])
        # Book Validations
        if len(postData['book_title']) == 0:
            errors['book_title'] = "Field cannot be left blank."
        # elif len(postData['book_title']) < 5:
        #     errors['book_title'] = "Book title cannot be fewer than 5 characters in length."
        elif len(postData['book_title']) > 50 :
            errors['book_title'] = "Book title cannot be longer than 50 characters in length."
        elif book:
            errors['book_title'] = "A book with that name already exists"

        return errors

class AuthorManager(models.Manager):
    def author_validator(self,postData):
        errors = {}

        author = Author.objects.filter(name=postData['new_author'])
        # Author Validations
        if len(postData['new_author']) == 0:
            errors['new_author'] = "Field cannot be left blank."
        # elif len(postData['new_author']) < 5:
        #     errors['new_author'] = "Author name cannot be fewer than 5 characters in length."
        elif len(postData['new_author']) > 50 :
            errors['new_author'] = "Author name cannot be longer than 50 characters in length."
        elif author:
            errors['new_author'] = "An author with that name already exists"

        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}

        # Text Validations
        if len(postData['new_review']) == 0:
            errors['new_review'] = "Field cannot be left blank."
        elif len(postData['new_review']) < 10:
            errors['new_review'] = "Review cannot be fewer than 10 characters in length."
        elif len(postData['new_review']) > 100:
            errors['new_review'] = "Review cannot be longer than 100 characters in length."

        # Rating Validations
        if int(postData['rating']) > 5 or int(postData['rating']) < 1:
                errors['rating'] = "Your rating can only be between 1 and 5 stars"
        
        # try:
        #     if int(postData['rating']) > 5 or int(postData['rating']) < 1:
        #         errors['rating'] = "Your rating can only be between 1 and 5 stars"
        # except:
        #     errors['rating'] = "Invalid rating. Stop hacking."
        
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    # authors_included: list of authors for this book
    # "book_reviews"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    authored_books = models.ManyToManyField(Book,related_name="authors_included")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

class Review(models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()