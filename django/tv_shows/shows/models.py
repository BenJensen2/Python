from django.db import models

class NetworkManager(models.Manager):
    def basic_validator(self,postData):




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

