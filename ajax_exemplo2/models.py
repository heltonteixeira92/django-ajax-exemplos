from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    bio = models.CharField(max_length=128)

    def __str__(self):
        return self.name
