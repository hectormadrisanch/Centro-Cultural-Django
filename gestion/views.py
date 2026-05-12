from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad
from .forms import ActividadForm

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'gestion/actividad_list.html', {'actividades': actividades})

# --- AÑADE ESTO NUEVO ---
def detalle_actividad(request, id):
    # Buscamos la actividad por su ID, o devolvemos un 404 si no existe
    actividad = get_object_or_404(Actividad, id=id)
    return render(request, 'gestion/actividad_detail.html', {'actividad': actividad})

def crear_actividad(request):
    if request.method == 'POST':
        # Si el usuario ha rellenado el formulario y le ha dado a guardar
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save() # ¡Magia! Se guarda en la base de datos
            return redirect('lista_actividades') # Lo devolvemos a la lista
    else:
        # Si solo está entrando a la página, le enseñamos el formulario vacío
        form = ActividadForm()
    
    return render(request, 'gestion/actividad_form.html', {'form': form})


def eliminar_actividad(request, id):
    # Buscamos la actividad que queremos borrar
    actividad = get_object_or_404(Actividad, id=id)
    
    if request.method == 'POST':
        # Si le da al botón de confirmar, la borramos y volvemos a la lista
        actividad.delete()
        return redirect('lista_actividades')
        
    # Si entra por primera vez, le enseñamos la pantalla de confirmación
    return render(request, 'gestion/actividad_confirm_delete.html', {'actividad': actividad})


def editar_actividad(request, id):
    # Buscamos la actividad que queremos editar
    actividad = get_object_or_404(Actividad, id=id)
    
    if request.method == 'POST':
        # Guardamos los cambios hechos sobre ESA actividad
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('detalle_actividad', id=actividad.id) # Volvemos al detalle
    else:
        # Le enseñamos el formulario pre-rellenado
        form = ActividadForm(instance=actividad)
    
    # ¡Reutilizamos el mismo archivo HTML que usamos para crear!
    return render(request, 'gestion/actividad_form.html', {'form': form, 'actividad': actividad})
