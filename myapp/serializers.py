from rest_framework import serializers
from .models import Subject, Teacher, Group, Student, GroupSubjectTeacher, TeacherSubject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class GroupSubjectTeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupSubjectTeacher
#         fields = '__all__'


class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = '__all__'


class GroupSubjectTeacherSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.first_name')
    subject_name = serializers.CharField(source='subject.name')
    teacher_last_name = serializers.CharField(source='teacher.last_name')

    class Meta:
        model = GroupSubjectTeacher
        fields = ['teacher_name', 'teacher_last_name', 'subject_name', 'day', 'time', 'location']

    def get_teacher_name(self, obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}" if obj.teacher else ""

    def get_subject_name(self, obj):
        return obj.subject.name if obj.subject else ""