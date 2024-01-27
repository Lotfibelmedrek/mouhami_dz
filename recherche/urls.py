from django.urls import path
from . import views


urlpatterns = [path('',views.search_lawyers),
               path('avocat_profile/<int:avocat_id>', views.AvocatDetailView.as_view(), name='lawyerr-detail'),

               ]


