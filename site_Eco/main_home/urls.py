from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('tests/', views.tests, name='individual_tests'),
    path('test/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('stocks/', views.actions, name='actions'),
    path('result/', views.result_quiz, name='results'),
    path('basket/', views.basket, name='basket')
]
