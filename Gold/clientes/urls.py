from . import views
from django.urls import path

urlpatterns = [      
    path('', views.clientes, name='clientes'),  
    path('cliente_status_/<int:cliente_id>/', views.change_status_clientes, name='cliente_status'), 
    path('create/', views.create_cliente, name='create_cliente'),                     
]   