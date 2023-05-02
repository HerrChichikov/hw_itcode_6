from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def all_workers(request):
    workers = Worker.objects.all()
    return render(request, 'core/all_workers.html', {'workers': workers, 'title': 'Главная'})


def best_worker(request):
    workers = Worker.objects.all()
    return render(request, 'core/best_worker.html', {'workers': workers, 'title': 'Сотрудник месяца'})
