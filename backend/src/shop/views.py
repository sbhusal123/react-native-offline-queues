from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
