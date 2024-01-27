from rest_framework import serializers
from .models import *
class Rendez_vousSerializer(serializers.ModelSerializer):
     class Meta:
        model=rendez_vous
        fields =['rendez_vousID','AvocatID','Date_rendezvous','accepted_yet','creneau_horraire']