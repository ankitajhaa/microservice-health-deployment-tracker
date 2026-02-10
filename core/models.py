"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password, **extra_fields):
        """Create, save and return user."""
        if not email:
            raise ValueError('Providing an email is compulsory')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """Create, save and return a superuser."""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.role = User.Roles.ADMIN
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    class Roles(models.TextChoices):
        ADMIN = "ADMIN"
        USER = "USER"

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
    )
    is_active = models.BooleanField('default=True')
    is_staff = models.BooleanField('default=False')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']