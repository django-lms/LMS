from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from core.students.models import Student
from api.serializers.students import StudentsSerializers


class StudentAPIView(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentsSerializers


class StudentDetailView(generics.RetrieveAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentsSerializers
    lookup_field = 'code'


class StudentCreateView(generics.CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentsSerializers

    def post(self, request):
        serializer = StudentsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('student_list')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)