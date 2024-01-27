from django.db import models
from register.models import *
class Evaluation(models.Model):
    AvocatID=models.ForeignKey(Avocats,on_delete=models.CASCADE,null=False)
    rating = models.PositiveIntegerField(null=True)
    confirmed = models.BooleanField(default=False,null=True)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    comment = models.TextField(null=True)