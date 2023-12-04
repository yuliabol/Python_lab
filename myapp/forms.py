from django import forms
from .models import Student, Teacher, GroupSubjectTeacher


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'group']
        labels = {
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'group': 'Група'
        }


class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
        }


class GroupSubjectTeacherForm(forms.ModelForm):
    class Meta:
        model = GroupSubjectTeacher
        fields = ['group', 'subject', 'teacher', 'type_lesson', 'day', 'time', 'location']