from django.urls import path

from api.views.teachers import TeacherListView, TeacherDetailView
from api.views.students import (
    StudentAPIView,
    StudentDetailView,
    StudentCreateView
)
from api.views.sections import SectionListView, SectionDetailView
from api.views.courses import CourseListAPIView, CourseDetailAPIView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name="teacher_list"),
    path('teachers/<uuid:pk>', TeacherDetailView.as_view()),
    path('students/', StudentAPIView.as_view(), name="student_list"),
    path('students/<code>', StudentDetailView.as_view()),
    path('student/create', StudentCreateView.as_view(), name="student_create"),
    path('courses/create/', CourseListAPIView.as_view(), name="course_create"),
    path('courses/<id>', CourseDetailAPIView.as_view(), name="course_detail"),
    path('courses/sections/', SectionListView.as_view(), name="section_list"),
    path('courses/sections/<int:pk>/', SectionDetailView.as_view(), name="section_detail"),
]
