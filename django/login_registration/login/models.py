from django.db import models
import re
# from app_name.models import *
# Only one direction: Model where the foreign key is.

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name needs to be at least 2 characters"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name needs to be at least 2 characters"
        # Birthday: validate is in the past
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        #  - Registered email should be unique
        if len(postData['pword']) < 8:
            errors['pword'] = "Password needs to be at least 8 characters long"
        if not postData['pword'] == postData['pword_confirm']:
            errors['pword_match'] = "Passwords don't match"
            # Need to encrypt password
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField()  # Figure out formatting for submission and display
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    # Encrypt within model: More Advanced Not Belt Exam

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()