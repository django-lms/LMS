from django.urls import path

from api.views.teachers import TeacherAPIView
from api.views.students import (
    StudentAPIView,
    StudentDetailView,
    StudentCreateView
)
from api.views.sections import SectionAPIView, SectionDetailView
from api.views.courses import CourseListAPIView, CourseDetailAPIView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view(), name="student_list"),
    path('students/<code>', StudentDetailView.as_view()),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('courses/create/', CourseListAPIView.as_view(), name="course_create"),
    path('courses/<id>', CourseDetailAPIView.as_view(), name="course_detail"),
    path('courses/sections/', SectionAPIView.as_view(), name="section_list"),
    path('courses/sections/<id>/', SectionDetailView.as_view(), name="section_detail"),
]
