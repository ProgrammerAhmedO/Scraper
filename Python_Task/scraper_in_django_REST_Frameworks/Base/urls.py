from django.urls import path
from .views import ScrapedDataListView, ScrapedDataDetailView

urlpatterns = [
    path('api/data/', ScrapedDataListView.as_view(), name='data-list'),
    path('api/data/<int:pk>/', ScrapedDataDetailView.as_view(), name='data-detail'),
]