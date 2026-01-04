from django.db import models
from django.conf import settings
from stores.models import Store
from products.models import Medicine

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    STATUS_CHOICES = [
        ("CREATED", "Created"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
    ]

    store = models.ForeignKey(
        Store,
        on_delete=models.PROTECT,
        related_name="orders"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="CREATED"
    )

    # 🔐 Audit field
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="orders_created"
    )

    # ⏱️ Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["store", "status"]),
        ]

    def __str__(self):
        return f"Order #{self.id} - {self.store.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("order", "medicine")

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"
