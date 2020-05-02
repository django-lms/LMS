from django.urls import path

from api.views.teachers import TeacherAPIView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),   
]
