from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


class Criar(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Criar')


class Atualizar(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Logout')
