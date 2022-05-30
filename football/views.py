from multiprocessing import context
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from football.models import Hrac


def index(request):

    num_hraci = Hrac.objects.all().count()

    hraci = Hrac.objects.order_by('prijmeni')[:3]

    context = {
        'num_hraci': num_hraci,
        'hraci': hraci,
    }

    return render(request, 'index.html', context=context)

class HracListView(ListView):
    model = Hrac

    context_object_name = 'hraci'
    template_name = 'list.html'

class HracDetailView(DetailView):
    model = Hrac

    context_object_name = 'hraci_detail'
    template_name = 'detail.html'