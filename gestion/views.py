from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad, Usuario, Monitor, Sala
from .forms import ActividadForm, UsuarioForm, MonitorForm, SalaForm, InscribirUsuarioForm

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


# vistas para usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gestion/usuario_list.html', {'usuarios': usuarios})

def detalle_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'gestion/usuario_detail.html', {'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'gestion/usuario_form.html', {'form': form})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalle_usuario', id=usuario.id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'gestion/usuario_form.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'gestion/usuario_confirm_delete.html', {'usuario': usuario})


# VISTAS PARA MONITORES
def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'gestion/monitor_list.html', {'monitores': monitores})

def detalle_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    return render(request, 'gestion/monitor_detail.html', {'monitor': monitor})

def crear_monitor(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_monitores')
    else:
        form = MonitorForm()
    return render(request, 'gestion/monitor_form.html', {'form': form})

def editar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('detalle_monitor', id=monitor.id)
    else:
        form = MonitorForm(instance=monitor)
    return render(request, 'gestion/monitor_form.html', {'form': form, 'monitor': monitor})

def eliminar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        monitor.delete()
        return redirect('lista_monitores')
    return render(request, 'gestion/monitor_confirm_delete.html', {'monitor': monitor})


# VISTAS PARA SALAS
def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'gestion/sala_list.html', {'salas': salas})

def detalle_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    return render(request, 'gestion/sala_detail.html', {'sala': sala})

def crear_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()
    return render(request, 'gestion/sala_form.html', {'form': form})

def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('detalle_sala', id=sala.id)
    else:
        form = SalaForm(instance=sala)
    return render(request, 'gestion/sala_form.html', {'form': form, 'sala': sala})

def eliminar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('lista_salas')
    return render(request, 'gestion/sala_confirm_delete.html', {'sala': sala})


# VISTAS PARA INSCRIPCIONES
def lista_inscripciones(request, id):
    # Cogemos la actividad específica
    actividad = get_object_or_404(Actividad, id=id)
    # Sacamos todos los usuarios apuntados a ESA actividad
    usuarios_apuntados = actividad.usuarios_inscritos.all()
    
    return render(request, 'gestion/inscripciones_list.html', {
        'actividad': actividad, 
        'usuarios': usuarios_apuntados
    })

def inscribir_usuario(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    
    if request.method == 'POST':
        form = InscribirUsuarioForm(request.POST)
        if form.is_valid():
            usuario_seleccionado = form.cleaned_data['usuario']
            # ¡La magia del N a N en Django! Añadimos el usuario a la actividad
            actividad.usuarios_inscritos.add(usuario_seleccionado)
            return redirect('lista_inscripciones', id=actividad.id)
    else:
        form = InscribirUsuarioForm()
        
    return render(request, 'gestion/inscribir_form.html', {'form': form, 'actividad': actividad})


def eliminar_inscripcion(request, id, usuario_id):
    actividad = get_object_or_404(Actividad, id=id)
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Desapuntamos al usuario de la actividad
    actividad.usuarios_inscritos.remove(usuario)
    
    # Volvemos a la lista de alumnos de ESA actividad
    return redirect('lista_inscripciones', id=actividad.id)