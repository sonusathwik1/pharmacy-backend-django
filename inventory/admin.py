from django.contrib import admin
from .models import Medicine, Batch, Stock


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'is_active')
    search_fields = ('name', 'manufacturer')
    list_filter = ('is_active',)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'batch_number', 'expiry_date', 'mrp')
    list_filter = ('expiry_date',)
    search_fields = ('batch_number', 'medicine__name')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('store', 'batch', 'quantity')
    list_filter = ('store',)
