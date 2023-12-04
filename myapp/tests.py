# from django.test import TestCase, RequestFactory
# from django.contrib.auth.models import User
# from myapp.views import TeacherScheduleView
# from myapp.models import GroupSubjectTeacher
#
# class TeacherScheduleViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.teacher_id = self.user.id
#         self.group_subject_teacher = GroupSubjectTeacher.objects.create(teacher_id=self.teacher_id)
#
#     def test_teacher_schedule_view(self):
#         request = self.factory.get('/teacher-schedule/')
#         request.user = self.user
#
#         response = TeacherScheduleView.as_view()(request)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'schedule_display_teacher.html')
#         self.assertIsNotNone(response.context_data['teacher_schedule'])

# from django.test import TestCase, RequestFactory
# from django.urls import reverse
# from django.http import JsonResponse
# from myapp.views import StudentRegistrationView
# from myapp.forms import StudentRegistrationForm
# from myapp.models import Group
#
#
# class StudentRegistrationViewTest(TestCase):
#     def setUp(self):
#         Group.objects.create(name="КН", year=4)
#
#     def test_valid_post_request(self):
#         data = {
#             'first_name': 'Юлія',
#             'last_name': 'Болюбаш',
#             'group_id': 1
#             # Додайте інші необхідні дані форми для успішного POST-запиту
#         }
#         response = self.client.post(reverse('student-registration'), data)
#         self.assertEqual(response.status_code, 302)  # Redirect status code
#         self.assertRedirects(response, reverse('schedule-display'))
#
#     def test_invalid_post_request(self):
#         data = {
#
#         }
#         response = self.client.post(reverse('student-registration'), data)
#         self.assertEqual(response.status_code, 400)
#         self.assertTrue('message' in response.json())



# class ScheduleDisplayViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.url = reverse('schedule-display')
#
#     def test_valid_query_parameters(self):
#         group = Group.objects.create(name='Group 1', year=2)
#         GroupSubjectTeacher.objects.create(group=group, day='Monday', time='10:00', location='Room 101')
#
#         request = self.factory.get(self.url, {'group': group.id, 'day': 'Monday'})
#         response = ScheduleDisplayView.as_view()(request)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context_data['schedule']), 1)
#
#     def test_invalid_query_parameters(self):
#         request = self.factory.get(self.url, {'group': '', 'day': ''})
#         response = ScheduleDisplayView.as_view()(request)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context_data['schedule']), 0)
#
# class TeacherRegistrationViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.url = reverse('teacher-registration')
#
#     def test_get_request(self):
#         # Створення GET-запиту до сторінки реєстрації вчителя
#         request = self.factory.get(self.url)
#         response = TeacherRegistrationView.as_view()(request)
#
#         # Перевірка, що сторінка повертає успішний статус та форму реєстрації
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'form')
#
#     def test_valid_post_request(self):
#         teacher = Teacher.objects.create(first_name='John', last_name='Doe')
#
#         data = {'first_name': 'John', 'last_name': 'Doe'}
#         request = self.factory.post(self.url, data)
#         response = TeacherRegistrationView.as_view()(request)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('schedule-display-teacher'))
#
#     def test_invalid_post_request(self):
#         data = {'first_name': 'Jane', 'last_name': 'Doe'}
#         request = self.factory.post(self.url, data)
#         response = TeacherRegistrationView.as_view()(request)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Teacher not found')
#
# class EditScheduleViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.url = reverse('edit-schedule')
#
#     def test_valid_post_request(self):
#         teacher_id = 1
#         group_id = 1
#         subject_id = 1
#         lesson_type = 'lecture'
#         GroupSubjectTeacher.objects.create(
#             teacher_id=teacher_id, group_id=group_id, subject_id=subject_id,
#             type_lesson=lesson_type, day='Monday', time='10:00', location='Room 101'
#         )
#
#         # Створення POST-запиту для редагування розкладу
#         data = {'day': 'Tuesday', 'time': '11:00 AM', 'location': 'Room 102'}
#         url_with_params = f'{self.url}/{group_id}/{subject_id}/{lesson_type}'
#         request = self.factory.post(url_with_params, data)
#         request.user = self.create_user_with_id(teacher_id)  # Підмінюємо користувача для тесту
#         response = EditScheduleView.as_view()(request, group_id=group_id, subject_id=subject_id, type_lesson=lesson_type)
#
#         # Перевірка, що розклад був успішно змінений
#         self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного редагування
#         edited_schedule = GroupSubjectTeacher.objects.get(
#             teacher_id=teacher_id, group_id=group_id, subject_id=subject_id, type_lesson=lesson_type
#         )
#         self.assertEqual(edited_schedule.day, 'Tuesday')
#         self.assertEqual(edited_schedule.time.strftime("%I:%M %p"), '11:00 AM')
#         self.assertEqual(edited_schedule.location, 'Room 102')
#
#     def test_invalid_post_request(self):
#         # Створення POST-запиту для редагування неіснуючого розкладу
#         data = {'day': 'Tuesday', 'time': '11:00 AM', 'location': 'Room 102'}
#         request = self.factory.post(self.url, data)
#         response = EditScheduleView.as_view()(request)
#
#         # Перевірка, що редагування не відбулося через відсутність розкладу
#         self.assertEqual(response.status_code, 302)

from django.test import TestCase, Client
from django.urls import reverse
from .models import Group, Student, Teacher, GroupSubjectTeacher  # Import your models here


class StudentRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('student-registration')  # Replace with your URL name

    def test_student_registration_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_registration.html')

    def test_student_registration_view_post_valid(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            # Add other fields from your StudentRegistrationForm
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Assuming redirection after successful registration
        # Add additional assertions to check if the student was actually created

    def test_student_registration_view_post_invalid(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue(response.context['form'].errors)


class ScheduleDisplayViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for this view
        Group.objects.create(name="TestGroup", year=2023)
        # Add more setup data as required

    def setUp(self):
        self.client = Client()
        self.url = reverse('schedule-display')  # Replace with your URL name

    def test_schedule_display_view_get_no_params(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule_display.html')
        self.assertIn('groups', response.context)
        # Add more assertions as needed

    def test_schedule_display_view_get_with_params(self):
        # Assuming 'group' and 'day' are the query params
        response = self.client.get(self.url + '?group=1&day=Monday')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule_display.html')
        # Verify that the context data is correct
        # Add more assertions as needed

