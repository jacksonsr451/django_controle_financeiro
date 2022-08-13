from django.urls import path

from .views import Resumo


urlpatterns = [
    path('resumo/<str:ano>/<str:mes>', Resumo.as_view())
]
