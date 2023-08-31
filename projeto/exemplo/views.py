# exemplo/views.py
from rest_framework import viewsets
from projeto.exemplo.models import Product
from projeto.exemplo.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer