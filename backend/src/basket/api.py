from rest_framework.routers import DefaultRouter

from . import views as basket_views

basket_router = DefaultRouter()
basket_router.register('api/basket', basket_views.BasketViewSet)

