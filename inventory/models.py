from django.db import models
from stores.models import Store


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    composition = models.TextField()
    manufacturer = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Batch(models.Model):
    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        related_name="batches"
    )
    batch_number = models.CharField(max_length=50)
    expiry_date = models.DateField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.medicine.name} - {self.batch_number}"


class Stock(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="stocks"
    )
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="stocks"
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.store} | {self.batch} | Qty: {self.quantity}"
