from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from register.models import * 
from register.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime, timedelta
from rest_framework import status
import jwt 

@csrf_exempt
@api_view(['POST'])
def Avocats_login(request):
    identifier = request.data.get('identifier', '')
    password = request.data.get('password', '')

    if '@' in identifier:
        identifier_field = 'email'
    else:
        identifier_field = 'phone_number'

    try:
        Avocat = Avocats.objects.get(**{identifier_field: identifier})
    except Avocat.DoesNotExist:
        return JsonResponse({'error': 'Avocat not found'}, status=404)

    if check_password(password, Avocats.password):
        payload = {
            'id': Avocats.id,
            'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS),
            'iat': datetime.utcnow(),
        }
        Avocats_serializer = AvocatsSerializer(Avocats)
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return JsonResponse({'message': 'Login successful', 'token': token,'avocat':Avocats.data}, status=200)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

def jwt_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.headers.get('Authorization', '').split(' ')[-1].strip()
        if not token:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            user_id = payload.get('id') 
            request.user = User.objects.get(pk=user_id)
        except jwt.ExpiredSignatureError:
            return render(request, 'token_expired.html')
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        return view_func(request, *args, **kwargs)

    return _wrapped_view



