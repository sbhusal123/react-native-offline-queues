from rest_framework.viewsets import ModelViewSet

from .serializers import BasketSerializer

from .models import Basket

from rest_framework.permissions import IsAuthenticated

class BasketViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_queryset(self):
        qs = Basket.objects.filter(user=self.request.user)
        return qs

    def get_serializer_context(self):
        context = super().get_serializer_context() 
        context["user"] = self.request.user
        return context