from django.urls import path
from .views import InventoryListAPIView

urlpatterns = [
    path('inventory/', InventoryListAPIView.as_view()),
]
