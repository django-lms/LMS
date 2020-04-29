from rest_framework import serializers
from core.courses import models


class CoursesSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(teacher=user)
    class Meta:
        fields = '__all__'
        model = models.Course


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Section
