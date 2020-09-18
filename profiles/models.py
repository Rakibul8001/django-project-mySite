from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    location = models.CharField(max_length=200, blank = True, null = True)
    job = models.CharField(max_length=120, null = True)

    def __str__(self):
        return self.name
