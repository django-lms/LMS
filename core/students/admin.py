from django.contrib import admin

# Register your models here.
from core.students.models import Student

admin.site.register(Student)