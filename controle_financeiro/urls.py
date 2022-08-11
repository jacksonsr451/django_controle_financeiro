from django.urls import path, include

urlpatterns = [
    path('', include('despesas.urls')),
    path('', include('receitas.urls')),
    path('', include('resumo.urls')),
]
