from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    # Core store details
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    store_code = models.CharField(max_length=20, unique=True)

    # Business relationships
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_stores",
    )

    # Status
    is_active = models.BooleanField(default=True)

    # 🔐 Audit fields (DAY 13 addition)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="stores_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.store_code}"
