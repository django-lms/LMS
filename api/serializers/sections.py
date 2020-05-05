from rest_framework import serializers

from core.courses.models import Section
from core.accounts.models import User


class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Section
        fields = '__all__'