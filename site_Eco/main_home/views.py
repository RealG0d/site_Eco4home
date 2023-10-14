from django.shortcuts import render

def home(request):
    return render(request, 'main_site/index.html')

def tests(request):
    return render(request, 'main_site/tests.html')

def catalog(request):
    return render(request, 'main_site/catalog.html')

def actions(request):
    return render(request, 'main_site/stocks.html')
