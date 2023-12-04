from django.shortcuts import render, redirect
from clientes.models import Cliente

def clientes(request):
    clientes_list = Cliente.objects.all()   
    return render(request, 'clientes/index.html', {'clientes_list': clientes_list})

def change_status_clientes(request, clientes_id):
    clientes = Cliente.objects.get(pk=clientes_id)
    clientes.status = not clientes.status
    clientes.save()
    return redirect('clientes')

# Create your views here.
