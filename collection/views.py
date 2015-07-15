from django.shortcuts import render
from .models import Mineral

def mineral_list(request):
    minerals = Mineral.objects.all().order_by('-id')
    context = {
        'minerals': minerals
    }

    if 'd' in request.GET:
        if request.GET.get('d') == 'mosaic':
            return render(request, 'collection/mosaic.html', context)

    return render(request, 'collection/list.html', context)

def mineral_detail(request, mineral_id):
    mineral = Mineral.objects.get(pk=mineral_id)
    context = {
        'mineral': mineral
    }

    return render(request, 'collection/detail.html', context)

