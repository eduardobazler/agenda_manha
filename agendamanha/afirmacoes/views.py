from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from agendamanha.afirmacoes.models import Afirmacao, AfirmacaoForm
from django.contrib import messages


def check_afirmacao_owner(afirmacao, request):
    if afirmacao.owner != request.user:
        raise Http404


@login_required
def afirmacoes(request):
    """Mostra todas as afirmações."""
    afirmacoes_list = Afirmacao.objects.filter(owner=request.user).order_by('date_added')

    paginator = Paginator(afirmacoes_list, 3)

    page = request.GET.get('page')

    afirmacoes = paginator.get_page(page)

    context = {'afirmacoes': afirmacoes}
    return render(request, 'afirmacoes/afirmacoes.html', context)


@login_required
def add_afirmcao(request):
    """Add nova afirmação"""
    if request.method != 'POST':
        form = AfirmacaoForm
    else:
        form = AfirmacaoForm(data=request.POST)
        if form.is_valid():
            nova_afirmacao = form.save(commit=False)
            nova_afirmacao.owner = request.user
            nova_afirmacao.save()
            return redirect('afirmacoes:afirmacoes')

    context = {'form': form}
    return render(request, 'afirmacoes/add_afirmacao.html', context)


@login_required
def edit_afirmacao(request, afirmacao_id):
    afirmacao = get_object_or_404(Afirmacao, id=afirmacao_id)

    check_afirmacao_owner(afirmacao, request)

    if request.method != 'POST':
        form = AfirmacaoForm(instance=afirmacao)
    else:
        form = AfirmacaoForm(instance=afirmacao, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('afirmacoes:afirmacoes')

    context = {'afirmacao': afirmacao, 'form': form}
    return render(request, 'afirmacoes/edit_afirmacao.html', context)


@login_required
def del_afirmacao(request, afirmacao_id):
    afirmacao = get_object_or_404(Afirmacao, id=afirmacao_id)

    check_afirmacao_owner(afirmacao, request)

    afirmacao.delete()

    messages.info(request, 'Afirmação deletada com sucesso.')

    return redirect('afirmacoes:afirmacoes')
