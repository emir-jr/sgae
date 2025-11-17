import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils import timezone
from .models import Enterprise, Sector, Box


@admin.register(Enterprise)
class EnterpAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

class VencimentoFilter(admin.SimpleListFilter):
    title = 'Vencimento'
    parameter_name = 'vencimento'

    def lookups(self, request, model_admin):
        return [
            ('vencida', 'Vencida'),
            ('nao_vencida', 'Não vencida'),
        ]

    def queryset(self, request, queryset):
        hoje = timezone.now().date()
        if self.value() == 'vencida':
            return queryset.filter(discard_date__lt=hoje)
        if self.value() == 'nao_vencida':
            return queryset.filter(discard_date__gte=hoje)
        return queryset


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'enterprise', 'sector', 'location', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'enterprise__name', 'sector__name',)
    list_filter = ('is_active','enterprise','sector', VencimentoFilter)

    def export_to_csv (self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'empresa', 'setor', 'localização', 'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.enterprise.name, product.sector.name, product.location, product.is_active, product.description, product.created_at, product.updated_at])
        return response
    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]

    def queryset(self, request, queryset):
        hoje = timezone.now().date()
        if self.value() == 'vencida':
            return queryset.filter(discard_date__lt=hoje)
        if self.value() == 'nao_vencida':
            return queryset.filter(discard_date__gte=hoje)
        return queryset
