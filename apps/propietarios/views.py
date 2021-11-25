from django.shortcuts import render, redirect
from apps.propietarios.models import Propietario
from apps.propietarios.form import PropietarioForm

def index(request):    
    propietario = Propietario.objects.all().order_by('-id')
    context = {'propietarios': propietario}
    return render(request, 'propietarios/index.html', context)


def home(request): 
    return render(request, 'base/base.html')

def propietarioCreate(request):   
    if(request.method == 'POST'):   
        form = PropietarioForm(request.POST)
        if form.is_valid():   
            form.save()
        return redirect('propietarios:index')
    else:   
        form = PropietarioForm()
        return render(request, 'propietarios/formPropietario.html',{'form': form})
    
    
def propietarioEdit(request, id_propietario):   
    propietario = Propietario.objects.get(pk=id_propietario)
    
    if request.method == 'GET':   
        form = PropietarioForm(instance=propietario)
    else:   
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():    
            form.save()
        return redirect('propietarios:index')
    return render(request, 'propietarios/formPropietario.html', {'form': form})


def propietarioDelete(request, id_propietario): 
    propietario = Propietario.objects.get(pk=id_propietario)
    if request.method == 'POST':   
        propietario.delete()
        return redirect('propietarios:index')
    return render(request, 'propietarios/propietarioEliminar.html', {'propietarios': propietario})

























