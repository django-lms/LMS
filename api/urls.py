from django.urls import path

from api.views.teachers import TeacherAPIView
from api.views.students import (
    StudentAPIView,
    StudentDetailView,
    StudentCreateView
)
from api.views.courses import SectionAPIView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view(), name="student_list"),
    path('students/<code>', StudentDetailView.as_view()),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('sections/', SectionAPIView.as_view()),
]
