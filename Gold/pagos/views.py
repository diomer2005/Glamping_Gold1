from django.shortcuts import render, redirect
from pagos.models import Pago
from .forms import PagoForm

def pagos(request):    
    pagos_list = Pago.objects.all()    
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def change_status_pago(request, pagos_id):
    pagos = Pago.objects.get(pk=pagos_id)
    pagos.status = not pagos.status
    pagos.save()
    return redirect('pagos')

def create_pago(request):
    form = PagoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagos')    
    return render(request, 'pagos/create.html', {'form': form})
# Create your views here.
