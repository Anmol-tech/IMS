from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampModel


class UserManager(BaseUserManager):
    """
    Base manager for custom user model.
    """

    def get_queryset(self):
        return super(UserManager, self).get_queryset()

    def _create_user(self, username, email, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))

        email = self.normalize_email(email)
        user = self.model(
            username=username, email=email, is_superuser=is_superuser, last_login=now, created_at=now, **extra_fields
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, **extra_fields)


class ImsUser(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    """
    Model for User

    Email and password are required. Other fields are optional.
    """
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    username = models.CharField(_('Username'), max_length=50, unique=True)
    email = models.EmailField(_('Email'), max_length=255)
    first_name = models.CharField(_('First Name'), max_length=50, blank=True, default='')
    middle_name = models.CharField(_('Middle Name'), max_length=50, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=50, blank=True, default='')

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.first_name.strip() + ' ' + self.last_name.strip()

    @property
    def is_staff(self):
        """
        Function to overwrite the unnecessary requirement of the is_staff field
        """
        return self.is_superuser
