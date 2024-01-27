from django.urls import path
from . import views

urlpatterns = [
    path('lawyer_login',views.Avocats_login),
]
