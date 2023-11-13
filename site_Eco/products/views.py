from django.shortcuts import render
from .models import *
from main_home.models import Plant
from django.views.generic import ListView
from django.http import JsonResponse


class PlantsListView(ListView):
    model = Plant
    template_name = 'products/catalog.html'
    context_object_name = 'items'
    paginate_by = 5


def load_more_data(request):
    page = request.GET.get('page', 1)
    items_per_page = 5
    start_index = (int(page) - 1) * items_per_page
    end_index = start_index + items_per_page

    queryset = Plant.objects.all()[start_index:end_index]
    data = list(queryset.values())

    return JsonResponse(data, safe=False)


def view_product(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    context = {
        'item': plant
    }

    session_key = request.session.session_key
    if not session_key:
        request.session['session_key'] = 123
        request.session.cycle_key()
        print(request.session.session_key)

    return render(request, 'products/product.html', context=context)
