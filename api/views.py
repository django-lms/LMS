from rest_framework import generics

from core.courses import models
from . import serializers


class ListCourses(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CoursesSerializer


class SectionCourses(generics.ListCreateAPIView):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class DetailCourses(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CoursesSerializer


class DetailSection(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
