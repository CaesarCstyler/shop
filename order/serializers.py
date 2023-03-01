from rest_framework import serializers
from order.models import Order
from order.send_email import send_order_confirmation_code

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        amount = validated_data.get('amount')
        product = validated_data.get('product')

        if amount > product.amount:
            raise serializers.ValidationError('Not enough product in warehouse')
        if amount == 0:
            raise serializers.ValidationError('Amount can not be 0')

        product.amount -= amount
        product.save(update_fields=['amount'])

        order = Order.objects.create(**validated_data)

        # send email
        send_order_confirmation_code(order.owner.email, order.activation_code, order.product.title, order.total_price)

        return order
