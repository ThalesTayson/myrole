from django.db import models
from users.models import Usuarios, Dados_pagamento, Enderecos

class Categorias ( models.Model ):
    descricao = models.CharField( max_length=50 )
    status = models.BooleanField( default=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

class Tipos_interessados ( models.Model ):
    descricao = models.CharField( max_length=70 )
    status = models.BooleanField( default=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
class Eventos ( models.Model ):
    nome = models.CharField( max_length=70 )
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    duracao = models.TimeField()
    foto = models.ImageField(upload_to='capas_eventos', default='padrao/sem_image.png')
    local = models.TextField( max_length=70 )
    endereco = models.ForeignKey(Enderecos, related_name='fk_endereco_evento', on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, related_name='fk_categoria', on_delete=models.PROTECT)
    dono_evento = models.ForeignKey(Usuarios, related_name='fk_dono', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
class Ingressos ( models.Model ):
    nome = models.CharField( max_length=50 )
    descricao = models.TextField()
    valor = models.DecimalField( decimal_places=2, max_digits=9)
    has_meia_entrada = models.BooleanField( default=True )
    meia_entrada = models.DecimalField( decimal_places=2, max_digits=9)
    quantidade = models.IntegerField()
    data_initial = models.DateTimeField()
    data_limit = models.DateTimeField()
    quantidade_minima_por_venda = models.IntegerField( )
    quantidade_maxima_por_venda = models.IntegerField( )
    evento = models.ForeignKey(Eventos, related_name='fk_evento', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
class Ingressos_x_interessados ( models.Model ):
    ingresso = models.ForeignKey(Ingressos, related_name='fk_ingresso_interessado', on_delete=models.CASCADE)
    tipo_interessado = models.ForeignKey(Tipos_interessados, related_name='fk_tipo_interessado', on_delete=models.PROTECT)

class Vendas ( models.Model ):
    quantidade = models.IntegerField()
    ingresso = models.ForeignKey(Ingressos, related_name='fk_ingresso', on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuarios, related_name='fk_venda_usuario', null=True, on_delete=models.SET_NULL)
    dados_pagamento = models.ForeignKey(Dados_pagamento, related_name='fk_dados_pag', null=True, on_delete=models.SET_NULL)