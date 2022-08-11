from django.urls import path

from .views import index


urlpatterns = [
    path('api/v1/despesas/', index),
]
