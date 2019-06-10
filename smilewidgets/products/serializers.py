from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from products.models import Product, GiftCard, ProductPrice

class ProductPriceSerializer(serializers.Serializer):
    productCode = serializers.CharField(max_length=10, source='product'),
    date = serializers.DateField(allow_null=False)
    giftCardCode = serializers.CharField(max_length=30, required=False, allow_null=True)