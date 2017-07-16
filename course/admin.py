from django.contrib import admin

from course.models import Student, Prof, Course


admin.site.register(Student)
admin.site.register(Prof)
admin.site.register(Course)
