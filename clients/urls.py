from django.urls import path
from . import views
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('create/', views.client_create, name='client_create'),
    path('edit/<int:pk>/', views.client_edit, name='client_edit'),
    path('api/clients/', ClientListCreateAPIView.as_view(), name='api_clients_list_create'),
    path('api/clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='api_clients_rud'),
]
                                                        