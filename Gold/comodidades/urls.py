from . import views
from django.urls import path

urlpatterns = [      
    path('', views.comodidades, name='comodidades'),   
    path('comodidad_status_/<int:comodidad_id>/', views.change_status_comodidad, name='comodidad_status'), 
    path('create/', views.create_comodidad, name='create_comodidad'),                           
]