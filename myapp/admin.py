from django.contrib import admin
from .models import Teacher, Subject, Group, GroupSubjectTeacher, Student


class GroupSubjectTeacherInline(admin.TabularInline):
    model = GroupSubjectTeacher


class TeacherAdmin(admin.ModelAdmin):
    inlines = [GroupSubjectTeacherInline]


# Реєстрація моделей
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(GroupSubjectTeacher)
admin.site.register(Student)

