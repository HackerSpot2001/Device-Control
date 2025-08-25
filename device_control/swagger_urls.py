from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        if request.scheme == "https":
            schema.schemes = schema.schemes.reverse()
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v3",
        description="API documentation for your Backend APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)

# url="https://backend.kaushalvikas.in/",

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
