import  uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = {
        ('lni-grid-alt', 'pet'),
        ('lni-ruler-pencil', 'almofada'),
        ('lni-customer', 'baby'),
        ('lni-support', 'outros'),
    }
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=50, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Produtos(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 350, 'crop': True}})
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class ProdutosCamaQ(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 350, 'crop': True}})
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'ProdutoCamaQ'
        verbose_name_plural = 'ProdutosCamaQ'

    def __str__(self):
        return self.nome


class ProdutosAlmofada(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 350, 'crop': True}})
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'ProdutoAlmofada'
        verbose_name_plural = 'ProdutosAlmofadas'

    def __str__(self):
        return self.nome


class ProdutosRoupasPet(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 350, 'crop': True}})
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'ProdutoRoupasPet'
        verbose_name_plural = 'ProdutosRoupasPet'

    def __str__(self):
        return self.nome


class ProdutosBercoBaby(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 350, 'crop': True}})
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'ProdutoBercoBaby'
        verbose_name_plural = 'ProdutosBercoBaby'

    def __str__(self):
        return self.nome


class Clientes(Base):
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 360, 'height': 250, 'crop': True}})
    nome = models.CharField('Nome', max_length=100, default=None)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
