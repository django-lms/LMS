import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = False
        user.is_staff = True
        user.type = 'A'
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.type = User.USER_TYPE_ADMIN
        user.save(using=self._db)
        return user


class User(AbstractUser):
    USER_TYPE_STUDENT = 1
    USER_TYPE_TEACHER = 2
    USER_TYPE_ADMIN = 3

    USER_TYPE = (
        (USER_TYPE_STUDENT, 'Student'),
        (USER_TYPE_TEACHER, 'Teacher'),
        (USER_TYPE_ADMIN, 'Admin'),
    )

    id = models.UUIDField(primary_key=True, editable=False,  default=uuid.uuid4)
    username = None
    email = models.EmailField(verbose_name='email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    type = models.SmallIntegerField(choices=USER_TYPE, default=USER_TYPE_ADMIN, verbose_name='type')

    objects = UserManager()



    @property
    def is_admin(self):
        return self.type == User.USER_TYPE_ADMIN

    @property
    def get_full_name(self):
        if not self.first_name:
            return "n/d".upper()

        return '%s, %s' % (self.last_name.upper(), self.first_name.upper())
