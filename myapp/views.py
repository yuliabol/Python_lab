from datetime import datetime

from django.http import JsonResponse
from rest_framework import generics
from .models import Subject, Teacher, Group, Student, GroupSubjectTeacher
from .serializers import GroupSubjectTeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.views import View


class APIRoot(APIView):
    def get(self, request):
        data = {
            'schedule': 'schedule_display/',
            'students_login': 'teacher/registration/',
            'teacher_login': 'student/registration/',
        }
        return Response(data)


class StudentRegistrationView(View):
    def get(self, request):
        form = StudentRegistrationForm()
        groups = Group.objects.all()
        return render(request, 'student_registration.html', {'form': form, 'groups': groups})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule-display')
        else:
            groups = Group.objects.all()
            return JsonResponse({'message': 'Invalid form data'}, status=400)
        groups = Group.objects.all()
        return render(request, 'student_registration.html', {'form': form, 'groups': groups})


class ScheduleDisplayView(generics.ListAPIView):
    serializer_class = GroupSubjectTeacherSerializer

    def get_queryset(self):
        group_id = self.request.GET.get('group')
        day = self.request.GET.get('day')

        if group_id and day:
            queryset = GroupSubjectTeacher.objects.filter(group_id=group_id, day=day)
            return queryset
        else:
            return GroupSubjectTeacher.objects.none()

    def get(self, request, *args, **kwargs):
        groups = Group.objects.all()
        student_name = request.user.username

        # Обробка запиту GET
        queryset = self.get_queryset()
        selected_day = request.GET.get('day')

        context = {
            'groups': groups,
            'student_name': student_name,
            'schedule': queryset,
            'selected_day': selected_day,
        }

        return render(request, 'schedule_display.html', context)


class TeacherRegistrationView(View):
    def get(self, request):
        form = TeacherRegistrationForm()
        return render(request, 'teacher_registration.html', {'form': form})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            teacher = Teacher.objects.get(first_name=first_name, last_name=last_name)
            return redirect('schedule-display-teacher')  # Перенаправлення на сторінку розкладу з використанням його ID
        except Teacher.DoesNotExist:
            return render(request, 'teacher_registration.html', {'error': 'Teacher not found'})


class TeacherScheduleView(View):
    def get(self, request):
        teacher_id = request.user.id - 1
        try:
            teacher_schedule = GroupSubjectTeacher.objects.filter(teacher_id=teacher_id)
        except GroupSubjectTeacher.DoesNotExist:
            teacher_schedule = None

        return render(request, 'schedule_display_teacher.html', {'teacher_schedule': teacher_schedule})


def convert_to_24_hour_format(time_str):
    parts = time_str.split(':')
    hour = int(parts[0])
    minute = int(parts[1].split()[0])

    if 'p' in time_str.lower() and hour < 12:
        hour += 12

    return f"{hour:02d}:{minute:02d}:00"


class EditScheduleView(View):
    def get(self, request, *args, **kwargs):
        teacher_id = request.user.id - 1  # Отримати ID викладача, який залогінений в систему
        group_id = kwargs.get('group_id')
        subject_id = kwargs.get('subject_id')
        type_lesson = kwargs.get('type_lesson')

        teacher_schedule_to_edit = GroupSubjectTeacher.objects.get(teacher_id=teacher_id, type_lesson=type_lesson,
                                                                   group_id=group_id, subject_id=subject_id)
        try:
            teacher_schedule = GroupSubjectTeacher.objects.filter(teacher_id=teacher_id)
        except GroupSubjectTeacher.DoesNotExist:
            teacher_schedule = None

        return render(request, 'edit_schedule.html', {'teacher_schedule_to_edit': teacher_schedule_to_edit})

    def post(self, request, *args, **kwargs):
        updated_day = request.POST.get('day')
        updated_time = request.POST.get('time')
        updated_time = convert_to_24_hour_format(updated_time)
        updated_location = request.POST.get('location')

        try:
            teacher_schedule_to_edit = GroupSubjectTeacher.objects.get(
                type_lesson=kwargs.get("type_lesson"),
                group_id=kwargs.get('group_id'),
                subject_id=kwargs.get('subject_id'),
            )
            print(teacher_schedule_to_edit.id)
            object_to_edit = GroupSubjectTeacher.objects.get(
                id=teacher_schedule_to_edit.id
            )
            #print(f"Group ID: {teacher_schedule_to_edit.group_id}, Subject ID: {teacher_schedule_to_edit.subject_id}, Lesson Type: {teacher_schedule_to_edit.type_lesson}")
            if updated_day and updated_time and updated_location:
                object_to_edit.day = updated_day
                object_to_edit.time = updated_time
                object_to_edit.location = updated_location

                print(object_to_edit)
                object_to_edit.save(update_fields=['day', 'time', 'location'])
        except GroupSubjectTeacher.DoesNotExist:
            pass

        return redirect('schedule-display-teacher')






