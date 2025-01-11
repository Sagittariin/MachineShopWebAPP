from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    # Automatically set the client based on the logged-in user
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Orders
        fields = ['part_number', 'quantity', 'plant', 'client']
        extra_kwargs = {
            'part_number': {'required': True},  # Ensure part number is required
            'quantity': {'min_value': 1, 'max_value': 99},  # Validate quantity range
            'plant': {'required': True},  # Ensure plant is required
        }

    def create(self, validated_data):
        # Automatically set the status to 'pending' and date_created
        validated_data['status'] = 'pending'
        return super().create(validated_data)
