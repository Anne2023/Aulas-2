from rest_framework import serializers
from projeto.exemplo.models import product

class ProductSerializer (serializers.ModelSerializer):
  class Meta:
    model = product
    field = ['id', 'title', 'descripition', 'price', 'quantity'] 