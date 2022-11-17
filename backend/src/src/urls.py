from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

# custom apps routers to be registered here
from shop.api import shop_router
from basket.api import basket_router

router = DefaultRouter()
router.registry.extend(shop_router.registry)
router.registry.extend(basket_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # JWT token views
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
