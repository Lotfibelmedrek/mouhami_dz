from django.urls import path
from . import views


urlpatterns = [
               path('create_rendez_vous', views.create_rendez_vous),
               path('taken_rendez_vous',views.taken_Rendez_vous)
               ]


