from django.urls import path
from . import views
from .views import ScheduleDisplayView, StudentRegistrationView, TeacherRegistrationView, \
    EditScheduleView, TeacherScheduleView  # TeacherScheduleUpdateView

urlpatterns = [
    path('api/', views.APIRoot.as_view(), name='api-root'),
    path('student/registration/', StudentRegistrationView.as_view(), name='student-registration'),
    path('teacher/registration/', TeacherRegistrationView.as_view(), name='teacher-registration'),
    path('schedule_display/', ScheduleDisplayView.as_view(), name='schedule-display'),
    path('edit_schedule/<int:group_id>/<int:subject_id>/<str:type_lesson>/', EditScheduleView.as_view(), name='edit-schedule'),
    path('teacher_schedule/', TeacherScheduleView.as_view(), name='schedule-display-teacher'),
    #path('teacher_schedule_update/<int:teacher_id>', TeacherScheduleUpdateView.as_view(), name='teacher_schedule_update'),
]
