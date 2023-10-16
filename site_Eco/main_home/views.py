import json

from django.core import serializers
from django.shortcuts import render
from .models import Plant
from django.views.generic import ListView
from django.core.paginator import Paginator

from django.http import JsonResponse

def home(request):
    return render(request, 'main_site/index.html')

def tests(request):
    return render(request, 'main_site/tests.html')

def catalog(request):
    items = Plant.objects.all()
    paginator = Paginator(items, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items': items,
        'page_obj': page_obj,
    }
    return render(request, 'main_site/catalog.html', context=context)

class PlantsListView(ListView):
    model = Plant
    template_name = 'main_site/catalog.html'
    context_object_name = 'items'
    paginate_by = 4


def load_more_data(request):
    page = request.GET.get('page', 1)
    items_per_page = 4
    start_index = (int(page) - 1) * items_per_page
    end_index = start_index + items_per_page

    queryset = Plant.objects.all()[start_index:end_index]
    data = list(queryset.values())

    return JsonResponse(data, safe=False)


def result_view(request):
    if request.method == 'POST':
        q1_answer = request.POST.get('q1')
        q2_answer = request.POST.get('q2')
        q3_answer = request.POST.get('q3')

        score = 0

        # Оценка ответов
        if q1_answer == 'a':
            score += 1
        if q2_answer == 'b':
            score += 1
        if q3_answer == 'c':
            score += 1

        # Определение результата
        if score == 3:
            result = "Отлично! Вы набрали максимальное количество очков!"
            recommended_product = "Полезный товар A"
        elif score == 2:
            result = "Хорошо! Вы набрали большинство очков!"
            recommended_product = "Полезный товар B"
        else:
            result = "Попробуйте еще раз. Вы набрали меньше очков."
            recommended_product = "Полезный товар C"

        return render(request, 'main_site/tests.html', {'result': result, 'recommended_product': recommended_product})

    return render(request, 'main_site/tests.html')

def actions(request):
    return render(request, 'main_site/stocks.html')
