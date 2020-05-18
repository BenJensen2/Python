from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}

        if len(postData['show_title']) < 2:
            errors['show_title'] = "Title should be at least 2 characters"
        if len(postData['show_network']) < 3:
            errors['show_network'] = "Network name should be at least 3 characters"
        if len(postData['show_description']) < 10:
            errors['show_description'] = " Description should be at least 10 characters"
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    # show_aired = list of movies on network

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.ForeignKey(Network, related_name="show_aired", on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

