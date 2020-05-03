from rest_framework import serializers

from core.courses.models import Section
from core.accounts.models import User


class SectionSerializers(serializers.ModelSerializer):
    #user = serializers.CharField(source='user.get_full_name')

    class Meta:
        model = Section
        fields = '__all__'