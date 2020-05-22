from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        not_blank = "This field cannot be left blank."
        fewer_2 = "This field cannot be fewer than 2 characters in length."
        longer_3 = "This field cannot be longer than 30 characters in length."
        invalid_email = "Invalid email address."
        
        # First Name Validations
        if len(postData['fname']) == 0:
            errors['fname'] = not_blank
        elif len(postData['fname']) < 2:
            errors['fname'] = fewer_2
        elif len(postData['fname']) > 30:
            errors['fname'] = longer_3

        # Last Name Validations
        if len(postData['lname']) == 0:
            errors['lname'] = not_blank
        elif len(postData['lname']) < 2:
            errors['lname'] = fewer_2
        elif len(postData['lname']) > 30:
            errors['lname'] = longer_3

        # Include Birthday Validations

        # Email Validations
        EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = not_blank
        elif len(postData['email']) < 6:
            errors['email'] = invalid_email
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = invalid_email
        elif user:
            errors['email'] = "Please use another email address."

        # Password Validations
        PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,16}$")
        if len(postData['pword']) == 0:
            errors['pword'] = not_blank
        elif len(postData['pword']) < 8:
            errors['pword'] = "Password must be at least 8 characters long."
        elif not PASS_REGEX.match(postData['password']):
            errors['pword'] = "Password must contain 1 uppercase, 1 lowercase, 1 number, and 1 special character."
        elif postData['pword'] != postData['pw_confirm']:
            errors['pword'] = "Passwords do not match."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # birthday = models.DateTimeField()
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    # "user_reviews"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
