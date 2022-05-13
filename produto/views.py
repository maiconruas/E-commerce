from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'


class DetalheProduto(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('DetalheProduto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('AdicionarAoCarrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('RemoverDoCarrinho')


class Carrinho(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Carrinho')


class Busca(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Busca')
