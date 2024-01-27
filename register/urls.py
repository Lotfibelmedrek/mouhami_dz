from django.urls import path
from . import views

urlpatterns=[
             path('submit_Avocat',views.AvocatsSignUpView.as_view()),
           ]