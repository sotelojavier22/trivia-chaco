from django.contrib import admin

from .models import Pregunta, Opcion, Respuesta

class OpcionEnLinea(admin.TabularInline):
    model = Opcion
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['enunciado', 'categoria', 'orden']}),
    ]
    inlines = [OpcionEnLinea]

admin.site.register(Pregunta,PreguntaAdmin)