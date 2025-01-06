from django.contrib import admin

from .models import Department, Posters, Student, Category, Result, Schedule, Image

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(Image)
admin.site.register(Posters)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('program', 'category', 'group')  # Fields to display in the admin listing
    search_fields = ('program', 'first_place__name', 'second_place__name', 'third_place__name')  # Enable search by related student names
    filter_horizontal = ('first_place', 'second_place', 'third_place')  # Adds a more user-friendly widget for ManyToMany fields
    list_filter = ('category', 'group')  # Filters for easier navigation

admin.site.register(Result, ResultAdmin)
