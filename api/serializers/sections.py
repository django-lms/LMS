from rest_framework import serializers

from core.courses.models import Section


class SectionCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id','name']


class SectionDetailSerializer(serializers.ModelSerializer):
    course = SectionCourseSerializer('course', read_only=True)
    
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name', read_only=True)
    
    class Meta:
        model = Section
        fields = '__all__'

        
class SectionCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Section
        fields = '__all__'