from django.shortcuts import render, redirect
from apps.viviendas.models import Vivienda
from apps.viviendas.form import ViviendaForm

def index(request):    
    vivienda = Vivienda.objects.all().order_by('-id')
    context = {'viviendas': vivienda}
    return render(request, 'viviendas/index.html', context)


def home(request): 
    return render(request, 'base/base.html')

def viviendaCreate(request):   
    if(request.method == 'POST'):   
        form = ViviendaForm(request.POST)
        if form.is_valid():   
            form.save()
            
        return redirect('viviendas:index')
    else:   
        form = ViviendaForm()
        return render(request, 'viviendas/formVivienda.html',{'form': form})

    
def viviendaEdit(request, id_vivienda):   
    vivienda = Vivienda.objects.get(pk=id_vivienda)
    
    if request.method == 'GET':   
        form = ViviendaForm(instance=vivienda)
    else:   
        form = ViviendaForm(request.POST, instance=vivienda)
        if form.is_valid():    
            form.save()
        return redirect('viviendas:index')
    return render(request, 'viviendas/formVivienda.html', {'form': form})


def viviendaDelete(request, id_vivienda): 
    vivienda = Vivienda.objects.get(pk=id_vivienda)
    if request.method == 'POST':   
        vivienda.delete()
        return redirect('viviendas:index')
    return render(request, 'viviendas/viviendaEliminar.html', {'viviendas': vivienda})

























