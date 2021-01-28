from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Сериалайзер для ордер айтемов"""
    class Meta:
        model = OrderItem
        exclude = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для ордера"""
    items = OrderItemSerializer(many=True)
    created_at = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = ('user',)

    def create(self, validated_data):
        """Создаем ордер проверя на валидность и сохраняем ордер для юзера"""
        request = self.context.get('request')
        items = validated_data.pop('items')
        validated_data['status'] = 'pending'
        order = Order.objects.create(**validated_data)
        order.user = request.user
        order.save()
        for item in items:
            item = OrderItem.objects.create(**item)
            order.items.add(item)
        return order
