from django.shortcuts import render, redirect
from agendamanha.afirmacoes.models import Afirmacao, AfirmacaoForm
from django.contrib import messages


def afirmacoes(request):
    """Mostra todas as afirmações."""
    afirmacoes = Afirmacao.objects.order_by('date_added')
    context = {'afirmacoes': afirmacoes}
    return render(request, 'afirmacoes/afirmacoes.html', context)


def add_afirmcao(request):
    """Add nova afirmação"""
    if request.method != 'POST':
        form = AfirmacaoForm
    else:
        form = AfirmacaoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('afirmacoes:afirmacoes')

    context = {'form': form}
    return render(request, 'afirmacoes/add_afirmacao.html', context)


def edit_afirmacao(request, afirmacao_id):
    afirmacao = Afirmacao.objects.get(id=afirmacao_id)

    if request.method != 'POST':
        form = AfirmacaoForm(instance=afirmacao)
    else:
        form = AfirmacaoForm(instance=afirmacao, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('afirmacoes:afirmacoes')

    context = {'afirmacao': afirmacao, 'form': form}
    return render(request, 'afirmacoes/edit_afirmacao.html', context)


def del_afirmacao(request, afirmacao_id):
    afirmacao = Afirmacao.objects.get(id=afirmacao_id)
    afirmacao.delete()

    messages.info(request, 'Afirmação deletada com sucesso.')

    return redirect('afirmacoes:afirmacoes')
