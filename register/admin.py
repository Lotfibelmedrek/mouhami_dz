from django.contrib import admin
from  register.models import*

@admin.register(Avocats)
class AvocatsAdmin(admin.ModelAdmin):
    list_display = ( 'nom_complet',  'email','password','numero_telephone', 'domaine_juridique','location','description','cv')
    search_fields = ( 'domaine_juridique','location')
