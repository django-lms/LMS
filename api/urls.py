from django.urls import path

from api.views.teachers import TeacherAPIView
from api.views.students import StudentAPIView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view()),

]
