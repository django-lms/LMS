from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ListCourses.as_view()),
    path('<uuid:pk>',views.DetailCourses.as_view()),
    path('section/',views.SectionCourses.as_view()),
    path('section/<int:pk>',views.DetailSection.as_view()),  
    path('rest-auth/',include('rest_auth.urls')),

]
