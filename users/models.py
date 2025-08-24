from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserLoginManager



primary_max_len=255
class UserLogin(AbstractUser):
    user_login_id = models.CharField(
        primary_key=True,
        unique=True,
        max_length=primary_max_len,
        editable=False,
        null=False,
    )
    password = models.CharField(max_length=255, null=False, blank=False)
    username = None
    last_updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "user_login_id"
    REQUIRED_FIELDS = ["password"]

    objects = UserLoginManager()

    def __str__(self):
        deleted_text = "Activated" if self.is_active else "Deactivated"
        return f"{self.user_login_id} | {self.get_full_name()} ({deleted_text})"


    class Meta:
        managed = True
        db_table = "user_login"
        ordering = ["-last_updated_at"]
        verbose_name_plural = "UserLogin"

