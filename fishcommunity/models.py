from django.db import models

# Create your models here.
class AnglerPost(models.Model):
    title = models.CharField(max_length=100)
    fish_species = models.CharField(max_length=100)
    lake_name = models.CharField(max_length=100)
    baits_used = models.CharField(max_length=100)  
    weather_conditions = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title