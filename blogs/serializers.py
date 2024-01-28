from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {'image': {'required': False}}