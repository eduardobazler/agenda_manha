from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from agendamanha.afirmacoes.models import Afirmacao


@register(Afirmacao)
class AfirmacaoAdmin(ModelAdmin):
    pass
