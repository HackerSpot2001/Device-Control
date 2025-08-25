from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from .views import AuthenticationViewSet


router = routers.DefaultRouter()
router.register(r"auth", AuthenticationViewSet, "Users Authentication")
# router.register(r"", UsersViewSet, "Users Master")

urlpatterns = router.urls
