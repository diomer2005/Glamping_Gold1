from django.shortcuts import render, redirect
from clientes.models import Cliente
from . forms import ClienteForm

def clientes(request):
    clientes_list = Cliente.objects.all()   
    return render(request, 'clientes/index.html', {'clientes_list': clientes_list})

def change_status_clientes(request, clientes_id):
    clientes = Cliente.objects.get(pk=clientes_id)
    clientes.status = not clientes.status
    clientes.save()
    return redirect('clientes')

def create_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')    
    return render(request, 'clientes/create.html', {'form': form})


# Create your views here.
