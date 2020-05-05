
from rest_framework import serializers

from core.teachers.models import Teacher
from core.accounts.models import User


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('user', 'code')
