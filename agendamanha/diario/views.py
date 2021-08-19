from django.contrib import messages
from django.shortcuts import render, redirect

from agendamanha.diario.models import Diario, DiarioForm


def diario(request):
    """Mostra todas as afirmações."""
    entradas = Diario.objects.order_by('date_added')
    entradas = entradas.reverse()
    context = {'entradas': entradas}
    return render(request, 'diario/diario.html', context)


def add_entrada(request):
    """Add nova entrada no diário"""
    if request.method != 'POST':
        form = DiarioForm
    else:
        form = DiarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('diario:diario')

    context = {'form': form}
    return render(request, 'diario/add_entrada.html', context)


def edit_entrada(request, entrada_id):
    entrada = Diario.objects.get(id=entrada_id)

    if request.method != 'POST':
        form = DiarioForm(instance=entrada)
    else:
        form = DiarioForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('diario:diario')

    context = {'entrada': entrada, 'form': form}
    return render(request, 'diario/edit_entrada.html', context)


def del_entrada(request, entrada_id):
    entrada = Diario.objects.get(id=entrada_id)
    entrada.delete()

    messages.info(request, 'Entrada do diário deletada com sucesso.')

    return redirect('diario:diario')
