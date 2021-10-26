from django.urls import path
from agendamanha.tarefas import views

app_name = 'tarefas'
urlpatterns = [
    path('', views.terefas, name='tarefas'),
    path('<int:tarefa_id>', views.terefa, name='tarefa'),
    path('add_tarefa', views.add_tarefa, name='add_tarefa'),
    path('edit_tarefa/<int:tarefa_id>', views.edit_tarefa, name='edit_terefa'),
    path('del_tarefa/<int:tarefa_id>', views.del_tarefa, name='del_tarefa'),

]
