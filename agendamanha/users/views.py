from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from agendamanha.users.models import CustomUserCreationForm


def sair_login(request):
    logout(request)
    return render(request, 'base/index.html')


def register(request):
    """ Registra um novo usuário """
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            login(request, new_user)
            return redirect('base:home')

    contex = {'form': form}
    return render(request, 'registration/register.html', contex)
