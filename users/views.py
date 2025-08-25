from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import login, logout, authenticate
from .serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from .models import UserLogin
from rest_framework.viewsets import ViewSet



class AuthenticationViewSet(ViewSet):
    http_method_names = ["get", "post", "options"]
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer


    @swagger_auto_schema(
        method="POST",
        operation_description="Login in Dash-board.",
        request_body=LoginSerializer,
    )
    @action(detail=False, methods=["post"], url_path="login")
    def auth_login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            err_message = ""
            for field, errors in serializer.errors.items():
                err_message += ", ".join(errors)

            return Response(
                {
                    "message": err_message,
                    "code": "EMPAPP_FAILED",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        validated_data = serializer.validated_data
        user = authenticate(
            request=request,
            username=validated_data.get("user_login_id"),
            password=validated_data.get("password"),
        )
        if user is None:
            return Response(
                {
                    "error": "Failed to login using provided credentials.",
                    "code": "AUTH_FAIL",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)
        return Response(
            {"message": "Login successful", "code": "AUTH_OK"},
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        method="POST",
        operation_description="Log-out in Dash-board.",
    )
    @action(detail=False, methods=["post"], url_path="logout")
    def auth_logout(self, request):
        logout(request)
        return Response(
            {"message": "Logout successful", "code": "AUTH_LOGOFF"},
            status=status.HTTP_200_OK,
        )




    # @swagger_auto_schema(
    #     method="GET",
    #     operation_description="Log-out in Dash-board.",
    # )
    # @action(detail=False, methods=["GET"], url_path="whoami")
    # @method_decorator(ensure_csrf_cookie)
    # def whoami(self, request):
    #     if request.user.is_authenticated:
    #         data = profileDetails(request.user.user_login_id)
    #         return Response(
    #             {
    #                 "message": "Operation completed successfully.",
    #                 "code": "AUTH_OK",
    #                 "record": data,
    #             },
    #             status=status.HTTP_200_OK,
    #         )

    #     return Response(
    #         {"message": "User is not logged-in", "code": "AUTH_LOGOFF"},
    #         status=status.HTTP_401_UNAUTHORIZED,
    #     )
