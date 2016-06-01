from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 120)
    price = serializers.FloatField()
    stock = serializers.FloatField()
    unit = serializers.CharField(max_length = 10)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.save()
        return instance
