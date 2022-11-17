from rest_framework.routers import DefaultRouter

from . import views as shop_views

shop_router = DefaultRouter()

shop_router.register(r'api/products', shop_views.ProductViewSet)