from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import QuizForm

from django.http import JsonResponse


def home(request):
    return render(request, 'main_site/index.html')

def tests(request):
    tests = Quiz.objects.all()
    context = {
        'tests': tests,
    }
    return render(request, 'main_site/tests.html', context=context)

def catalog(request):
    items = Plant.objects.all()
    paginator = Paginator(items, 1)
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
    paginate_by = 5


def load_more_data(request):
    page = request.GET.get('page', 1)
    items_per_page = 5
    start_index = (int(page) - 1) * items_per_page
    end_index = start_index + items_per_page

    queryset = Plant.objects.all()[start_index:end_index]
    data = list(queryset.values())

    return JsonResponse(data, safe=False)

def actions(request):
    return render(request, 'main_site/stocks.html')


def quiz_view(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(category=quiz)

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            category = ''
            qes_1, qes_2, qes_3 = 0, 0, 0
            for question in questions:
                selected_answer_id = form.cleaned_data[f'question_{question.id}']
                selected_answer = Answer.objects.get(pk=selected_answer_id)
                if selected_answer.score_ans == 1:
                    qes_1 += 1
                elif selected_answer.score_ans == 2:
                    qes_2 += 1
                else:
                    qes_3 += 1

            if qes_1 >= 1 or qes_3 >= 1:
                category = 'Декоративно-лиственные растения'
            elif qes_2 == 2:
                category = 'Кактусы и суккуленты'

            return result_quiz(request, category)

    else:
        form = QuizForm(questions=questions)

    return render(request, 'main_site/test.html', {'quiz': quiz, 'form': form, 'questions': questions})

def result_quiz(request, category):
    if category == 'Декоративно-лиственные растения':
        good_plants = Plant.objects.filter(type_plant=category)
    elif category == 'Кактусы и суккуленты':
        good_plants = Plant.objects.filter(type_plant=category)
    else:
        good_plants = Plant.objects.all()

    return render(request, 'main_site/result.html', {'good_plants': good_plants})
