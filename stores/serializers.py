from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'city', 'store_code', 'is_active']
def validate_store_code(self, value):
        """
        Business validation:
        Store code must be alphanumeric and unique.
        """
        if not value.isalnum():
            raise serializers.ValidationError(
                "Store code must be alphanumeric."
            )
        return value