from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('despesas.urls')),
    path('api/v1/', include('receitas.urls')),
    path('api/v1/', include('resumo.urls')),
]
