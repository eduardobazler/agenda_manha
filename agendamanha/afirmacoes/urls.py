from django.urls import path
from agendamanha.afirmacoes import views

app_name = 'afirmacoes'
urlpatterns = [
    path('', views.afirmacoes, name='afirmacoes'),
    path('add_afirmacao', views.add_afirmcao, name='add_afirmacao'),
    path('edit_afirmacao/<int:afirmacao_id>', views.edit_afirmacao, name='edit_afirmacao'),
    path('del_afirmacao/<int:afirmacao_id>', views.del_afirmacao, name='del_afirmacao'),
]
