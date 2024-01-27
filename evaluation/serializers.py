from rest_framework import serializers
from .models import  Evaluation
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('AvocatID', 'rating', 'confirmed', 'name', 'email', 'comment')