from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

from storage.views import *

urlpatterns = [
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/goods/', GoodsAPIList.as_view()),
    path('api/v1/goods/<int:pk>/', GoodsAPIUpdate.as_view()),
    path('api/v1/goodsdelete/<int:pk>/', GoodsAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
