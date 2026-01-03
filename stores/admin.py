from django.contrib import admin
from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_code', 'name', 'city', 'manager', 'is_active')
    list_filter = ('city', 'is_active')
    search_fields = ('store_code', 'name')
    ordering = ('store_code',)

def has_delete_permission(self, request, obj=None):
    return request.user.is_superuser
