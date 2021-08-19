from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from agendamanha.diario.models import Diario


@register(Diario)
class DiarioAdmin(ModelAdmin):
    pass
