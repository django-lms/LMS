from rest_framework import generics

from core.teachers.models import Teacher
from api.serializers.teachers import TeacherSerializer

class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer