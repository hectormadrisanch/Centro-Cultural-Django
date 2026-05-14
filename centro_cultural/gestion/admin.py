from django.contrib import admin
from .models import Monitor, ResponsableSala, Sala, Usuario, Actividad

admin.site.register(Monitor)
admin.site.register(ResponsableSala)
admin.site.register(Sala)
admin.site.register(Usuario)
admin.site.register(Actividad)