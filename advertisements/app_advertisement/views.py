from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ('Джанго-сервер успешно запушен! Поздравляю!')

