from django.urls import path

from .views import Despesas, DespesasByID


urlpatterns = [
    path('despesas/', Despesas.as_view()),
    path('despesas/<int:id>/', DespesasByID.as_view()),
]
