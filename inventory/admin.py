from django.contrib import admin
from .models import Medicine, Batch, Stock


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manufacturer",
        "is_active",
        "created_by",
        "created_at",
    )
    search_fields = ("name", "manufacturer")
    list_filter = ("is_active",)
    ordering = ("name",)

    # 🔐 Audit fields should not be editable
    readonly_fields = (
        "created_by",
        "created_at",
        "updated_at",
    )

    # 🔐 Auto-set created_by
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = (
        "medicine",
        "batch_number",
        "expiry_date",
        "mrp",
        "created_by",
        "created_at",
    )
    list_filter = ("expiry_date",)
    search_fields = ("batch_number", "medicine__name")
    ordering = ("expiry_date",)

    readonly_fields = (
        "created_by",
        "created_at",
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        "store",
        "batch",
        "quantity",
        "created_by",
        "updated_at",
    )
    list_filter = ("store",)
    ordering = ("store",)

    readonly_fields = (
        "created_by",
        "created_at",
        "updated_at",
    )

    # 🔐 Prevent manual inventory creation mistakes
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
