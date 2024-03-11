from django.shortcuts import render
from .models import Produto, Cliente

# crie as sua views aqui


def index(request):
    produtos = Produto.objects.all()

    text = {
        'noticias': 'Estou aprendendo Django em Python',
        'agradecimento': 'Graças a Deus',
        'produtos': produtos,
        'tabela': 'LISTA DE PRODUTOS'
    }

    return render(request, 'index.html', text,)


def contato(request):
    clientes = Cliente.objects.all()

    contatos = {
        'clientes': clientes
    }

    return render(request, 'contato.html', contatos)

