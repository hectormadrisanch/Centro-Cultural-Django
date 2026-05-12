from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'  # Esto le dice a Django: "Pon todos los campos en el formulario"