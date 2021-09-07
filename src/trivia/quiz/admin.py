from django.contrib import admin
from django.db import models
from django.db.models.fields import IntegerField

from .models import Pregunta, Opcion, Partida

class OpcionEnLinea(admin.TabularInline):
    model = Opcion
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['enunciado', 'categoria', 'orden']}),
    ]
    inlines = [OpcionEnLinea]
    list_display= ['enunciado','categoria','orden']

admin.site.register(Pregunta,PreguntaAdmin)

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.http import JsonResponse
from django.urls import path
from django.db.models.functions import TruncDay

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ("id","puntaje_total","fecha")
    ordering = ("-fecha",)
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Partida.objects.annotate(date=TruncDay("fecha"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
