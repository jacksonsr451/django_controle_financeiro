from django.urls import path

from .views import Receitas, ReceitasByID


urlpatterns = [
    path('receitas/', Receitas.as_view()),
    path('receitas/<int:id>/', ReceitasByID.as_view()),
]
