from django.db import models
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Photo for character_id:  @{self.url}"

   