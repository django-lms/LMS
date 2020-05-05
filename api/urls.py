from django.urls import path

from api.views.teachers import TeacherAPIView, TeacherDetailView
from api.views.students import (
    StudentAPIView,
    StudentDetailView,
    StudentCreateView
)
from api.views.courses import SectionListView, SectionDetailView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view(), name="teacher_list"),
    path('teachers/<uuid:pk>', TeacherDetailView.as_view()),
    path('students/', StudentAPIView.as_view(), name="student_list"),
    path('students/<code>', StudentDetailView.as_view()),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('courses/sections/', SectionListView.as_view(), name="section_list"),
    path('courses/sections/<int:pk>/', SectionDetailView.as_view(), name="section_detail"),
]
