from django.db import models
from django.conf import settings 
from apps.commons.models import BaseModel 

class Categoria(BaseModel):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True) 
        
    def __str__(self): 
        return self.nome 

class Local(BaseModel): 
    nome =  models.CharField(max_length=100 , unique=True)   
    descricao = models.TextField(blank=True) 
        

    def __str__(self): 
        return self.nome 

class Objeto(BaseModel): 
    TIPO_CHOICES = [
        ("PERDIDO","perdido"), 
        ("ENCONTRADO", "encontrado"), 
    ] 

    STATUS_CHOICES = [
        ("PENDENTE", "pendente"), 
        ("DEVOLVIDO", "devolvido"),
    ]

    nome = models.CharField(max_length=100)

    descricao = models.TextField() 
           
    tipo = models.CharField(max_length=10, 
    choices=TIPO_CHOICES) 

    status = models.CharField(max_length=10,
    choices=STATUS_CHOICES) 

    foto = models.ImageField(upload_to="objetos/", 
    blank=True, 
    null=True)

    usuario = models.ForeignKey( 
settings.AUTH_USER_MODEL, 
on_delete= models.CASCADE, 
        related_name="objetos"
    ) 

    categoria = models.ForeignKey(
        Categoria,
on_delete = models.PROTECT,
        related_name = "objetos"
)

    local = models.ForeignKey(
        Local, 
on_delete = models.PROTECT,
        related_name = "objetos"
    ) 

    def __str__(self): 
        return self.nome 
        