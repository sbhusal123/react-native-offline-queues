from rest_framework import serializers

from .models import Basket

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['quantity', 'product', 'id']


    def create(self, validated_data):
        user = self.context['user']
        basket = Basket.objects.create(**validated_data, user=user)
        return basket
