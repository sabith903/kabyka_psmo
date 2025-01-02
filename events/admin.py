from django.contrib import admin

from .models import Department, Student, Category, Result, Schedule, Image

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Result)
admin.site.register(Schedule)
admin.site.register(Image)
