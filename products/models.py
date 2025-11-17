from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Empresa'
    
    def __str__(self):
        return self.name

class Sector(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Setor'

    def __str__(self):
        return self.name

class Box (models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, related_name='products', verbose_name='Empresa')
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name='products', verbose_name='Setor')
    location = models.IntegerField(verbose_name='Localização')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    discard_date = models.DateField(null=True, blank=True, verbose_name='Data de Descarte')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Caixa'
    
    def __str__(self):
        return self.title

    