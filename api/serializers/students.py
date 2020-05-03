from rest_framework import serializers,generics

from core.students.models import Student
from core.accounts.models import User


class StudentsSerializers(serializers.ModelSerializer):
    user = serializers.CharField(source='user.get_full_name')

    class Meta:
        model = Student
        fields = '__all__'
