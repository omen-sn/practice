from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from storage import views
from storage.swagger import schema_view

router = DefaultRouter()
router.register(r'goods', views.GoodsViewSet, basename="goods")
router.register(r'categories', views.CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

'''urlpatterns = [
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/goods/', GoodsList.as_view()),
    path('api/v1/goods/<int:pk>/', GoodsDetail.as_view()),
    #path('api/v1/auth/', include('djoser.urls')),
    #re_path(r'^auth/', include('djoser.urls.authtoken')),
]'''

#urlpatterns = format_suffix_patterns(urlpatterns)
