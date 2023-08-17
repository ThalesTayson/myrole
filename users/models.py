from django.db import models
from django.contrib.auth.models import AbstractUser

class Enderecos_geral ( models.Model ):
    rua = models.CharField( max_length=70 )
    bairro = models.CharField( max_length=70 )
    cidade = models.CharField( max_length=70 )
    estado = models.CharField( max_length=70 )
    pais = models.CharField( max_length=70 )
    cep = models.CharField( max_length=20, unique=True, null=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_together = ('rua', 'bairro', 'cidade', 'estado', 'pais', 'cep')

class Enderecos ( models.Model ):
    numero = models.IntegerField( null=True )
    complemento = models.CharField( max_length=20, null=True )
    referencia = models.CharField( max_length=30, null=True )
    geral = models.ForeignKey(Enderecos_geral, related_name="fk_endereco_geral", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_together = ('numero', 'complemento', 'referencia', 'geral')
        
class Cod_paises ( models.Model ):
    code = models.CharField( max_length=4, primary_key=True, unique=True )
    pais = models.CharField( max_length=70, unique=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return '+' + self.code + ' - ' + self.pais
    
class Telefones ( models.Model ):
    cod_pais = models.ForeignKey(Cod_paises, related_name="fk_cod_pais", on_delete=models.PROTECT, default='55')
    cod_estado = models.CharField(max_length=3, default='67')
    numero = models.CharField(max_length=11)
    is_whats = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return f'+{self.cod_pais.code} {self.cod_estado} {self.numero}'

class Orientacao_sexual ( models.Model ):
    descricao = models.CharField( max_length=50, unique=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
class Usuarios ( AbstractUser ):
    # herdará username
    # herdará password
    # herdará email
    # herdará first_name
    # herdará last_name
    status = models.BooleanField( default = True )
    is_staff = models.BooleanField( default = False ) #Tira o Acesso do Django Admin
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    cpf = models.CharField( max_length=11, unique=True, null=True )
    cod_est = models.CharField( max_length=20, unique=True, null=True )
    orientacao_sexual = models.ForeignKey(Orientacao_sexual, related_name="fk_orientacao_sexual", null=True, on_delete=models.SET_NULL)
    celular = models.ForeignKey(Telefones, related_name="fk_celular", on_delete=models.PROTECT)
    whatsapp = models.ForeignKey(Telefones, related_name="fk_whatsapp", on_delete=models.PROTECT)
    endereco = models.ForeignKey(Enderecos, related_name="fk_endereco_usuario", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class Bandeiras_cartoes ( models.Model ):
    descricao = models.CharField( max_length=50 )
    status = models.BooleanField( default=True )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

class Dados_pagamento ( models.Model ):
    numero = models.CharField( max_length=50 )
    seguranca = models.CharField( max_length=10 )
    nome_cartao = models.CharField( max_length=70 )
    bandeira = models.ForeignKey(Bandeiras_cartoes, related_name='fk_bandeira', on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuarios, related_name='fk_dados_pagamento_usuario', on_delete=models.CASCADE)