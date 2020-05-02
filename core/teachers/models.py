import uuid

from django.db import models
from core.accounts.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    code = models.CharField(max_length=7, default="T" + uuid.uuid4().hex.upper()[0:6], blank=True,
                            verbose_name="Teacher code")

    def __str__(self):
        return self.user.get_full_name