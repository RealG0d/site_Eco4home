from django.urls import path
from . import views
from .views import PlantsListView, load_more_data

urlpatterns = [
    path('', PlantsListView.as_view(), name='catalog'),
    path('product/<int:plant_id>', views.view_product, name='product'),
    path('load-more-data/', load_more_data, name='load-more-data'),
]
