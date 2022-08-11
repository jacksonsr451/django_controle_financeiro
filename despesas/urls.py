from django.urls import path

from .views import Despesas


urlpatterns = [
    path('despesas/', Despesas.as_view()),
]
