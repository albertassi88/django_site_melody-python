from django.contrib import admin
from .models import Servico, Clientes, Produtos, ProdutosBercoBaby, ProdutosAlmofada, ProdutosRoupasPet, ProdutosCamaQ


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('modificado', 'imagem', 'nome')


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'nome', 'imagem', 'preco')


@admin.register(ProdutosCamaQ)
class ProdutosCamaQAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'nome', 'imagem', 'preco')


@admin.register(ProdutosRoupasPet)
class ProdutosRoupasPetAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'nome', 'imagem', 'preco')


@admin.register(ProdutosAlmofada)
class ProdutosAlmofadaAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'nome', 'imagem', 'preco')


@admin.register(ProdutosBercoBaby)
class ProdutosBercoBabyAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'nome', 'imagem', 'preco')