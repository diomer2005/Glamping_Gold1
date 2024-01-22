from django.shortcuts import render, redirect
from comodidades.models import Comodidad
from .forms import ComodidadForm

def comodidades(request):
    comodidades_list = Comodidad.objects.all()  
    return render(request, 'comodidades/index.html',{'comodidades_list': comodidades_list}
)
def change_status_comodidad(request, comodidades_id):
    comodidades = Comodidad.objects.get(pk=comodidades_id)
    comodidades.status = not comodidades.status
    comodidades.save()
    return redirect('comodidades')


def create_comodidad(request):
    form = ComodidadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('comodidades')    
    return render(request, 'comodidades/create.html', {'form': form})

# Create your views here.
