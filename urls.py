from django.urls import path
from .views import IndexView, EntregaDevolucaoView, SobreNosView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('entrega_devolucao', EntregaDevolucaoView.as_view(), name='entrega_devolucao'),
    path('sobre_nos', SobreNosView.as_view(), name='sobre_nos'),
]

