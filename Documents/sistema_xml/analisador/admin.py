# analisador/admin.py

from django.contrib import admin
from .models import Empresa, Produto, NotaFiscal, ItemNotaFiscal

# Registrando os modelos para que apareçam na interface de admin
admin.site.register(Empresa)
admin.site.register(Produto)
admin.site.register(NotaFiscal)
admin.site.register(ItemNotaFiscal)