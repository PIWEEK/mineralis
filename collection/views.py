from django.shortcuts import render
from .models import Mineral

def mineral_list(request):
    minerals = Mineral.objects.all().order_by('-id')
    context = {
        'minerals': minerals
    }
    return render(request, 'collection/list.html', context)

def mineral_detail(request, mineral_id):
    mineral = Mineral.objects.get(pk=mineral_id)
    context = {
        'mineral': mineral
    }
    return render(request, 'collection/detail.html', context)

