from django.contrib import admin
from courses.models import Course

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ("name", "available")
  list_filter = ("available",)
  search_fields = ("name", "description")