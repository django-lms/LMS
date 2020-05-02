from rest_framework import generics

from core.students.models import Student
from api.serializers.students import StudentsSerializers

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers
