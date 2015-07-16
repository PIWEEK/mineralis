from django.shortcuts import render
from .models import Mineral

def mineral_list(request):
    minerals = Mineral.objects.all().order_by('name')
    context = {
        'minerals': minerals
    }

    template = 'collection/kind.html'
    if 'd' in request.GET and request.GET.get('d') == 'mosaic':
        template = 'collection/mosaic.html'

    if 'k' in request.GET:
        context['minerals'] = minerals.filter(kind=request.GET.get('k'))
        context['kind'] = request.GET.get('k')

    return render(request, template, context)

def mineral_detail(request, mineral_id):
    minerals = Mineral.objects.all().order_by('name')
    if 'k' in request.GET and request.GET.get('k') != None:
        minerals = minerals.filter(kind=request.GET.get('k'))
    mineral = minerals.get(pk=mineral_id)
    minerals_ids = list(minerals.values_list('id', flat = True))
    mineral_ind = minerals_ids.index(int(mineral_id))
    mineral_prev = mineral_ind > 0 and minerals_ids[mineral_ind - 1] or None
    mineral_next = mineral_ind < len(minerals) -1 and minerals_ids[mineral_ind + 1] or None

    context = {
        'mineral': mineral,
        'mineral_prev': mineral_prev,
        'mineral_next': mineral_next
    }

    return render(request, 'collection/detail.html', context)
