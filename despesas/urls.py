from django.urls import path

from .views import Despesas, DespesasByAnoAndMes, DespesasByID


urlpatterns = [
    path('despesas/', Despesas.as_view()),
    path('despesas/<int:id>/', DespesasByID.as_view()),
    path('despesas/<str:ano>/<str:mes>/', DespesasByAnoAndMes.as_view()),
]
