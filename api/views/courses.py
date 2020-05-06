from rest_framework import generics

from core.courses.models import Section
from api.serializers.courses import SectionSerializers


class SectionAPIView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SectionDetailView(generics.RetrieveAPIView):
    queryset=Section.objects.all()
    serializer_class = SectionSerializers
    lookup_field='id'

