from django.contrib import admin
from django.urls import path, include
from .swagger_urls import urlpatterns as swagger_urls
from .template_views import home_page, login_page

urlpatterns = [
    path('login', view=login_page , name="Login Page"),
    # path('', view=home_page , name="Home Page"),
    # path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
] + swagger_urls

