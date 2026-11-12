from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AnglerPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='angler_posts')
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

class Comment(models.Model):
    post = models.ForeignKey(AnglerPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

class Likes(models.Model):
    post = models.ForeignKey(AnglerPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

     def __str__(self):
        return f'Like by {self.user} on {self.post.title}'

class AnglerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ConservationInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title