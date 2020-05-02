from rest_framework import serializers

from core.teachers.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('user', 'code')