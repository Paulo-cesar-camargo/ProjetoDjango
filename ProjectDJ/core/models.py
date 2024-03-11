from django.db import models


class Produto(models.Model):
    objects = None
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome


class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    objects = None
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

