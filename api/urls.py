from django.urls import path
from .views import PortList, TrajetEstimate

urlpatterns = [
    path('api/ports/', PortList.as_view(), name='ports-list'),
    path('api/trajets/', TrajetEstimate.as_view(), name='trajet-estimate'),
]
