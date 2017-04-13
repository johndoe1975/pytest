from django.contrib import admin

# Register your models here.

from .models import Student, Group

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'captain']
    inlines = [StudentInline]

admin.site.register(Student)
admin.site.register(Group, GroupAdmin)