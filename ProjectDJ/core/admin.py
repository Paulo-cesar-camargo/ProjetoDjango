from django.contrib import admin

# registre aqui os seus models
from .models import Produto, Clientes, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Cliente, ClienteAdmin)

