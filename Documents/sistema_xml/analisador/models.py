from django.db import models # essencial para definir modelos

class Empresa(models.Model):
    """Representa uma empresa, seja emitente ou destinatária."""
    cnpj = models.CharField(max_length=14, unique=True, help_text="CNPJ da empresa (apenas números)")
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

class Produto(models.Model):
    """Representa um produto que pode constar em uma NFe."""
    codigo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class NotaFiscal(models.Model):
    """Representa a NFe como um todo."""
    chave_acesso = models.CharField(max_length=44, unique=True, primary_key=True, help_text="Chave de Acesso da NFe com 44 dígitos")
    numero = models.IntegerField()
    serie = models.IntegerField()
    data_emissao = models.DateTimeField()
    
    emitente = models.ForeignKey(
        Empresa, 
        on_delete=models.PROTECT, 
        related_name='notas_emitidas'
    )
    destinatario = models.ForeignKey(
        Empresa, 
        on_delete=models.PROTECT, 
        related_name='notas_recebidas'
    )
    
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"NFe nº {self.numero} - {self.emitente.razao_social}"

    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais"

class ItemNotaFiscal(models.Model):
    """Representa um item específico dentro de uma Nota Fiscal."""
    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    
    quantidade = models.DecimalField(max_digits=15, decimal_places=4)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=4)
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Item {self.produto.descricao} da NFe {self.nota_fiscal.numero}"

    class Meta:
        verbose_name = "Item da Nota Fiscal"
        verbose_name_plural = "Itens da Nota Fiscal"
        unique_together = ('nota_fiscal', 'produto')