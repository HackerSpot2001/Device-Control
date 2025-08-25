from django.contrib import admin
from django.urls import path, include
from .swagger_urls import urlpatterns as swagger_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
] + swagger_urls

