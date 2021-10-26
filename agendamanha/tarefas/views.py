from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Tarefa
from .forms import TarefaForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def terefas(request):

    search = request.GET.get('search')

    if search:

        tarefas = Tarefa.objects.filter(titulo__icontains=search)

    else:
        tarefas_list = Tarefa.objects.all().order_by('-created_at')

        paginator = Paginator(tarefas_list, 5)

        page = request.GET.get('page')

        tarefas = paginator.get_page(page)

    contexto = {'tarefas': tarefas}

    return render(request, 'tarefas/tarefas.html', contexto)


def terefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    contexto = {'tarefa': tarefa}
    return render(request,'tarefas/tarefa.html', contexto)


def add_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.done = 'fazendo'
            tarefa.save()

            return redirect('tarefas:tarefas')

    else:
        form = TarefaForm()
        contexto = {'form': form}
    return render(request, 'tarefas/add_tarefa.html', contexto)


def edit_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            tarefa.save()
            return redirect('tarefas:tarefas')

        else:
            contexto = {'form': form, 'tarefa': tarefa}
            return render(request, 'tarefas/edit_tarefas.html', contexto)

    else:
        contexto = {'form': form, 'tarefa': tarefa}
        return render(request, 'tarefas/edit_tarefas.html', contexto)


def del_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    tarefa.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('tarefas:tarefas')