import uuid

from django.db import models

from core.accounts.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    code = models.CharField(max_length=7, default="S" + uuid.uuid4().hex.upper()[0:6], blank=True,
                            verbose_name="Student code")


    def __str__(self):
        return self.code
