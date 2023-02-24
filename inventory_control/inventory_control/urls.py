from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storage.urls')),
]
