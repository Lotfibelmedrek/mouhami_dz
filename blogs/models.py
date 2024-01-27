from django.db import models
from register.models import *
class Blog(models.Model):
    AvocatID = models.ForeignKey(Avocats, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
