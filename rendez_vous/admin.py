from django.contrib import admin
from .models import *
@admin.register(rendez_vous)
class Rendez_vousAdmin(admin.ModelAdmin):
    list_display=('AvocatID','Date_rendezvous','accepted_yet')
    search_fields=('userID','AvocatID')