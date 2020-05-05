from rest_framework import generics

from core.courses.models import Section
from api.serializers.courses import SectionListSerializer,SectionCreateUpdateSerializer,SectionDetailSerializer


class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return SectionCreateUpdateSerializer
        return SectionListSerializer


class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Section.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return SectionCreateUpdateSerializer
        if self.request.method == 'GET':
            return SectionDetailSerializer    
        return SectionListSerializer
