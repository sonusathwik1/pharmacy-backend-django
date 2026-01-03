from django.db import transaction
from inventory.models import Stock

@transaction.atomic
def confirm_order(order):
    for item in order.items.all():
        stock = Stock.objects.select_for_update().get(
            store=order.store,
            medicine=item.medicine
        )

        if stock.quantity < item.quantity:
            raise ValueError("Insufficient stock")

        stock.quantity -= item.quantity
        stock.save()

    order.status = "CONFIRMED"
    order.save()
