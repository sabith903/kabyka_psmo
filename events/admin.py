from django.contrib import admin

from .models import Department, Posters, Student, Category, Result, Schedule, Image

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(Image)
admin.site.register(Posters)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('program', 'category', 'group')  
    search_fields = ('program', 'first_place__name', 'second_place__name', 'third_place__name')  
    filter_horizontal = ('first_place', 'second_place', 'third_place') 

admin.site.register(Result, ResultAdmin)
