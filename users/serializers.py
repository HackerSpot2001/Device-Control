from rest_framework.serializers import Serializer, CharField, ValidationError, EmailField
from .models import UserLogin
from django.db.models import Q

class LoginSerializer(Serializer):
    user_login_id = CharField(required=True, max_length=100)
    password = CharField(required=True, max_length=100)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        login_id = attrs.get("user_login_id")

        emp_qs = UserLogin.objects.filter(user_login_id=login_id)

        if not emp_qs.exists():
            raise ValidationError(
                {"invalid_user_login": "Invalid user-login."}
            )

        return attrs


class RegisterSerializer(Serializer):
    username = CharField(required=True, max_length=100)
    password = CharField(required=True, max_length=100)
    con_pass = CharField(required=True, max_length=100)
    firstName = CharField(required=True, max_length=100)
    lastName = CharField(required=True, max_length=100)
    email = EmailField(required=True, max_length=100)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        login_id = attrs.get("user_login_id")
        emailId = attrs.get("email")

        emp_qs = UserLogin.objects.filter(Q(user_login_id=login_id) | Q(email=emailId))

        if emp_qs.exists():
            raise ValidationError(
                {"user_already_exists": "User-login/Email already exists."}
            )

        return attrs

