from django.urls import path, include
from agendamanha.users import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sair_login', views.sair_login, name='sair_login'),
    path('register/', views.register, name='register'),

]
