from rest_framework import serializers

from .models import Dog, Breed, Curator, Payment


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'birth_date', 'breed', 'curator', 'fixed')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', )


class CuratorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100, source='get_full_name', read_only=True)

    class Meta:
        model = Curator
        fields = ('id', 'name', 'surname', 'full_name')


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'date', 'number', 'amount', 'dog', 'transaction_id', 'purpose')
