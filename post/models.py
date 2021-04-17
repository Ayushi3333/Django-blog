from django.db import models

# Create your models here.

# adding attributes to the models below

class BlogPost(models.Model):
    # id = models.IntegerField() #pk
    title = models.TextField()
    slug = models.SlugField(unique=True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)