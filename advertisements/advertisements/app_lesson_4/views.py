from django.shortcuts import render
from django.http import HttpResponse

def index_1(request):
    return HttpResponse ('Домашка по 4 занятию')

