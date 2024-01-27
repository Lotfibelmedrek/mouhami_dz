from .views import  EvaluationListCreateView, EvaluationDetailView
from django.urls import path
from . import views


urlpatterns = [
    path('evaluations', EvaluationListCreateView.as_view(), name='evaluation'),
    path('evaluations/<int:pk>/', EvaluationDetailView.as_view(), name='evaluation-detail'),
]
