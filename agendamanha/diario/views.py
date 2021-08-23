from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from agendamanha.diario.models import Diario, DiarioForm


def check_entrada_owner(entrada, request):
    if entrada.owner != request.user:
        raise Http404


@login_required
def diario(request):
    """Mostra todas as afirmações."""
    entradas = Diario.objects.filter(owner=request.user).order_by('date_added')
    entradas = entradas.reverse()
    context = {'entradas': entradas}
    return render(request, 'diario/diario.html', context)


@login_required
def add_entrada(request):
    """Add nova entrada no diário"""
    if request.method != 'POST':
        form = DiarioForm
    else:
        form = DiarioForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.owner = request.user
            nova_entrada.save()
            return redirect('diario:diario')

    context = {'form': form}
    return render(request, 'diario/add_entrada.html', context)


@login_required
def edit_entrada(request, entrada_id):
    entrada = Diario.objects.get(id=entrada_id)

    check_entrada_owner(entrada, request)

    if request.method != 'POST':
        form = DiarioForm(instance=entrada)
    else:
        form = DiarioForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('diario:diario')

    context = {'entrada': entrada, 'form': form}
    return render(request, 'diario/edit_entrada.html', context)


@login_required
def del_entrada(request, entrada_id):
    entrada = Diario.objects.get(id=entrada_id)

    check_entrada_owner(entrada, request)

    entrada.delete()

    messages.info(request, 'Entrada do diário deletada com sucesso.')

    return redirect('diario:diario')
