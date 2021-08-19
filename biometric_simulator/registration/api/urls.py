from django.urls import path
from registration.api.api import  register_api_view, register_detail_api_view

urlpatterns = [
    path('listado_registros/',register_api_view, name = 'register_api_view'),
    path('registro/<int:pk>/',register_detail_api_view, name = 'register_detail_api_view')
]