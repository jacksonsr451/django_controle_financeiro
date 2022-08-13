from django.urls import path

from .views import Receitas, ReceitasByAnoAndMes, ReceitasByID


urlpatterns = [
    path('receitas/', Receitas.as_view()),
    path('receitas/<int:id>/', ReceitasByID.as_view()),
    path('receitas/<str:ano>/<str:mes>/', ReceitasByAnoAndMes.as_view()),
]
