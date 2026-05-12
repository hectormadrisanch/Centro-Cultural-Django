from django import forms
from .models import Actividad, Usuario, Monitor

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'  

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'