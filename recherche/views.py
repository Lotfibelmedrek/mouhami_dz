from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from register.models import Avocats
from register.serializers import *
from login.views import jwt_required

@api_view(['GET'])
def search_lawyers(request):
    Probleme_juridique = request.query_params.get('domaine_juridique', '')
    location = request.query_params.get('location', '')

   
    conditions = Q()

    if Probleme_juridique:
        conditions |= Q(Probleme_juridique__iexact=Probleme_juridique)
    if location:
        conditions |= Q(location__iexact=location)

    if not any([Probleme_juridique,  location]):
        return Response({'error': 'Please provide at least one search criteria'}, status=400)

    avocats = Avocats.objects.filter(conditions)

    serializer = AvocatsSerializer(Avocats, many=True)
    return Response(serializer.data, status=200)


class AvocatDetailView(APIView):
    def get(self, request, avocat_id, *args, **kwargs):
       
        lawyer = get_object_or_404(Avocats, id=avocat_id)

       
        lawyer_serializer = AvocatsSerializer(lawyer)

       
        return Response(lawyer_serializer.data, status=status.HTTP_200_OK)