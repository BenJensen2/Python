from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    # authors_included: list of authors for this book

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    authored_books = models.ManyToManyField(books,related_name="authors_included")