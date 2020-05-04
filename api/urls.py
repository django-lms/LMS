from django.urls import path

from api.views.teachers import TeacherAPIView
from api.views.students import (
    StudentAPIView,
    StudentDetailView,
    StudentCreateView
)
from api.views.courses import SectionAPIView, SectionDetailView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view(), name="student_list"),
    path('students/<code>', StudentDetailView.as_view()),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('courses/sections/', SectionAPIView.as_view(), name="section_list"),
    path('courses/sections/<id>/', SectionDetailView.as_view(), name="section_detail"),
]
