from rest_framework import serializers 
from .models import *
from django.contrib.auth.hashers import make_password

class AvocatsSerializer(serializers.ModelSerializer):
    class Meta :
        model=Avocats
        fields=('id','nom_complet','email','password','numero_telephone','domaine_juridique','location','description','cv')    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(AvocatsSerializer, self).create(validated_data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','first_name','last_name','email','password','is_active')
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
        