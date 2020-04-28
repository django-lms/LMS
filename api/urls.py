from django.urls import path,include
from . import views
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API LMS",
      default_version='v',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('',views.ListCourses.as_view()),
    path('<uuid:pk>',views.DetailCourses.as_view()),
    path('section/',views.SectionCourses.as_view()),
    path('section/<int:pk>',views.DetailSection.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]
