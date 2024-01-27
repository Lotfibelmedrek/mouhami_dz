from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *



class AvocatsSignUpView(generics.CreateAPIView):
    queryset = Avocats.objects.all()
    serializer_class = AvocatsSerializer
    
    def create(self, request, *args, **kwargs):
      
        email = request.data.get('email', None)

        
        if Avocats.objects.filter(email=email).exists():
            return Response({'error': 'Lawyer with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Continue with the creation process if the email is unique
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
def index3(request):
    return render(request,'index3.html')

def index4(request):
    return render(request,'index4.html')

