from django.contrib import admin
from .models import Profile,Student

admin.site.register (Profile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','address','email')
    list_filter = ('age',)
    ordering = ('age',)
    search_fields = ('name', 'email')
    list_per_page = 2
admin.site.register(Student, StudentAdmin)

# Register your models here.
