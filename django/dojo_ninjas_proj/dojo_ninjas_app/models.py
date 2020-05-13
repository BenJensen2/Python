from django.db import models

class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    # ninjas = List of ninjas
    desc = models.CharField(max_length=255)

class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(dojos, related_name="ninjas", on_delete=models.CASCADE)
    # dojo_id to assign the ninja to a dojo