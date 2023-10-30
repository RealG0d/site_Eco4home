from django.urls import path
from . import views
from .views import PlantsListView, load_more_data

urlpatterns = [
    path('', views.home, name='home_page'),
    path('tests/', views.tests, name='individual_tests'),
    path('test/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('catalog/', PlantsListView.as_view(), name='catalog'),
    path('load-more-data/', load_more_data, name='load-more-data'),
    path('stocks/', views.actions, name='actions'),
    path('result/', views.result_quiz, name='results'),
    path('product/<int:plant_id>', views.view_product, name='product'),
    path('basket/', views.basket, name='basket')
]
