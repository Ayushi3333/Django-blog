from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# adding attributes to the models below

class BlogPost(models.Model):
    # id = models.IntegerField() #pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
