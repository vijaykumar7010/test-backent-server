from rest_framework import serializers
from .models import NewProducts

class NewProductsserializer(serializers.ModelSerializer):
    class Meta:
        model = NewProducts
        fields = '__all__'