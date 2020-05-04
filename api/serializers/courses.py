from rest_framework import serializers

from core.courses.models import Section, Course
from core.accounts.models import User


class SectionSerializers(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name')
    
    class Meta:
        model = Section
        fields = '__all__'