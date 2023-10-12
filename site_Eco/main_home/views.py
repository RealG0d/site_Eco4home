from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main_site/index.html')

def about(request):
    return HttpResponse('<h1>Hehehehehe</h1>')
