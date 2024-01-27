from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from register.models import Avocats
from register.serializers import AvocatsSerializer  
from login.views import jwt_required
from .models import*
from .serializers import *

@api_view(['POST'])
@jwt_required
def create_rendez_vous(request, *args, **kwargs):
    avocat_id = request.data.get('avocat_id')
    Date_rendezvous = request.data.get('Date_rendezvous')
    
    
    print(avocat_id, Date_rendezvous)
    existing_rendez_vous_avocat = Avocats.objects.filter(
       AcocatID=avocat_id,
        Date_rendezvous=Date_rendezvous,
    ).first()

    if existing_rendez_vous_avocat:
        return Response({'error': "The advocate already has an appointment at this time and day."},
                        status=status.HTTP_400_BAD_REQUEST)

    advocate = get_object_or_404(Avocats, id=avocat_id)

    appointment_data = {
        'AvocatID': avocat_id,
        'Date_rendezvous':Date_rendezvous,
        'accepted_yet': False
    }
    serializer = AvocatsSerializer(data=appointment_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def taken_Rendez_vous(request):
    Avocat_id = request.query_params.get('Avocat_id')
    print(Avocat_id)
    taken_appointments = rendez_vous.objects.filter(AvocatID=Avocat_id, accepted_yet=False)
    print(taken_appointments)
    serializer = AvocatsSerializer(taken_appointments, many=True)
    print(serializer.data)

    return Response(serializer.data)

