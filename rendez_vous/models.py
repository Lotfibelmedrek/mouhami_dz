from django.db import models
from register.models import *
from django.utils import timezone
class rendez_vous(models.Model):
    Rendez_vousID=models.IntegerField
    AvocatID=models.ForeignKey(Avocats,on_delete=models.CASCADE)
    Date_rendezvous = models.DateTimeField(default=timezone.now)
    accepted_yet=models.BooleanField(default='False',blank=True,null=True)

