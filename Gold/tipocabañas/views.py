from django.shortcuts import render, redirect
from tipocabañas.models import Tipocabaña

def tipocabañas(request):
    tipocabañas_list = Tipocabaña.objects.all()
    return render(request, 'tipocabañas/index.html', {'tipocabañas_list': tipocabañas_list}
)

def change_status_tipocabaña(request, tipocabaña_id):
    tipocabaña = Tipocabaña.objects.get(pk=tipocabaña_id)
    tipocabaña.status = not tipocabañas.status
    tipocabaña.save()
    return redirect('tipocabañas')

from .forms import TipocabañaForm

def create_tipocabaña(request):
    form = TipocabañaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tipocabañas')    
    return render(request, 'tipocabañas/create.html', {'form': form})

# Create your views here.
