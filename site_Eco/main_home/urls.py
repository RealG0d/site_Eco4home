from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('tests/', views.tests, name='individual_tests'),
    path('catalog/', views.catalog, name='catalog')
]