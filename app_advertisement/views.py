from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

#def index(request):
    #return HttpResponse ('Джанго-сервер успешно запушен! Поздравляю!')

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context=context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


