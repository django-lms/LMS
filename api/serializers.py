from rest_framework import serializers
from core.courses import models


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Course


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Section 
