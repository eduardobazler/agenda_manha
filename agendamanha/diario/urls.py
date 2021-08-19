from django.urls import path
from agendamanha.diario import views

app_name = 'diario'
urlpatterns = [
    path('', views.diario, name='diario'),
    path('add_entrada', views.add_entrada, name='add_entrada'),
    path('edit_entrada/<int:entrada_id>', views.edit_entrada, name='edit_entrada'),
    path('del_entrada/<int:entrada_id>', views.del_entrada, name='del_entrada'),
]
