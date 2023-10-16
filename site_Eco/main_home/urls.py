from django.urls import path
from . import views
from .views import PlantsListView, load_more_data, result_view

urlpatterns = [
    path('', views.home, name='home_page'),
    path('tests/', views.tests, name='individual_tests'),
    # path('catalog/', views.catalog, name='catalog'),
    path('catalog/', PlantsListView.as_view(), name='catalog'),
    path('load-more-data/', load_more_data, name='load-more-data'),
    path('result/', result_view, name='result'),
    path('stocks/', views.actions, name='actions'),
]