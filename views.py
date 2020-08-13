from django.views.generic import TemplateView
from .models import Servico, Produtos, Clientes, ProdutosBercoBaby, ProdutosAlmofada, ProdutosCamaQ, ProdutosRoupasPet


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['produtos_nuvem'] = Produtos.objects.order_by('?').all()
        context['produtos_camaq'] = ProdutosCamaQ.objects.order_by('?').all()
        context['produtos_almofada'] = ProdutosAlmofada.objects.order_by('?').all()
        context['produtos_berco_baby'] = ProdutosBercoBaby.objects.order_by('?').all()
        context['produtos_roupas_pet'] = ProdutosRoupasPet.objects.order_by('?').all()
        context['clientes'] = Clientes.objects.order_by('?').all()
        return context


class EntregaDevolucaoView(TemplateView):
    template_name = 'entrega_devolucao.html'


class SobreNosView(TemplateView):
    template_name = 'sobre_nos.html'