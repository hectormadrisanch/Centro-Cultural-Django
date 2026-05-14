from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad, Usuario, Monitor, Sala
from .forms import ActividadForm, UsuarioForm, MonitorForm, SalaForm, InscribirUsuarioForm

def home(request):
    return render(request, 'gestion/home.html')

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'gestion/actividad_list.html', {'actividades': actividades})

def detalle_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    return render(request, 'gestion/actividad_detail.html', {'actividad': actividad})

def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_actividades') 
    else:
        form = ActividadForm()
    
    return render(request, 'gestion/actividad_form.html', {'form': form})

def programacion_semanal(request):
    actividades = Actividad.objects.all()
    return render(request, 'gestion/programacion.html', {'actividades': actividades})

def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    
    if request.method == 'POST':
        actividad.delete()
        return redirect('lista_actividades')
        
    return render(request, 'gestion/actividad_confirm_delete.html', {'actividad': actividad})


def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('detalle_actividad', id=actividad.id)
    else:
        form = ActividadForm(instance=actividad)
    
    return render(request, 'gestion/actividad_form.html', {'form': form, 'actividad': actividad})


# vistas para usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    actividades_lista = Actividad.objects.all()
    
    query_actividad = request.GET.get('actividad')
    if query_actividad:
        usuarios = usuarios.filter(actividades__id=query_actividad)
        
    return render(request, 'gestion/usuario_list.html', {
        'usuarios': usuarios, 
        'actividades_lista': actividades_lista
    })


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
    actividad = get_object_or_404(Actividad, id=id)
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
            actividad.usuarios_inscritos.add(usuario_seleccionado)
            return redirect('lista_inscripciones', id=actividad.id)
    else:
        form = InscribirUsuarioForm()
        
    return render(request, 'gestion/inscribir_form.html', {'form': form, 'actividad': actividad})


def eliminar_inscripcion(request, id, usuario_id):
    actividad = get_object_or_404(Actividad, id=id)
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    actividad.usuarios_inscritos.remove(usuario)
    
    return redirect('lista_inscripciones', id=actividad.id)

def lista_actividades(request):
    actividades = Actividad.objects.all()
    monitores = Monitor.objects.all()
    
    query_nombre = request.GET.get('q') 
    query_tipo = request.GET.get('tipo')
    
    
    if query_nombre:
        actividades = actividades.filter(nombre__icontains=query_nombre)
        
   
    if query_tipo:
        actividades = actividades.filter(tipo__icontains=query_tipo)
        
    query_monitor = request.GET.get('monitor')
    if query_monitor:
        actividades = actividades.filter(monitor__id=query_monitor)

    return render(request, 'gestion/actividad_list.html', {'actividades': actividades, 'monitores': monitores})