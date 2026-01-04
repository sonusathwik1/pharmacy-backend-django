from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("medicine", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "store",
        "status",
        "created_by",
        "created_at",
    )
    list_filter = ("status", "store")
    ordering = ("-created_at",)

    readonly_fields = (
        "created_by",
        "created_at",
        "updated_at",
    )

    inlines = [OrderItemInline]

    # 🚫 Prevent deleting confirmed orders
    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == "CONFIRMED":
            return False
        return True

    # 🔐 Auto-set created_by
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
