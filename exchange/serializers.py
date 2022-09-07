from rest_framework import serializers

from exchange.models import Gold, Silver


class GoldModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = [
            'id',
            'last',
            'bid',
            'ask',
            'high',
            'low',
            'open',
            'previousClose',
            'timestamp',

            'price_g',
            'price_kg',
            'previousClose_g',
            'previousClose_kg',

        ]

    def validate(self, data):
        pass

    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)

    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data)


class SilverModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silver
        fields = [
            'id',
            'last',
            'bid',
            'ask',
            'high',
            'low',
            'open',
            'previousClose',
            'timestamp',

            'price_g',
            'price_kg',
            'previousClose_g',
            'previousClose_kg',
        ]

    def validate(self, data):
        pass

    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)

    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data)
