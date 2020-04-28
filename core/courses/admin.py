from django.contrib import admin

# Register your models here.
from core.courses.models import *

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Resources)
admin.site.register(Package)
