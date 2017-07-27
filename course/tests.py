from django.test import TestCase
from django.test.client import Client

from course.models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        ali = Student.objects.create(first_name='ali', last_name='alavi', student_number='92100715',
                                     national_code='0019154356')
        reza = Student.objects.create(first_name='reza', last_name='bani', student_number='92100772',
                                      national_code='0019154123')

    def test_add_student_form(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get("add_student/")
        self.assertIs(response.status_code, 200)

    def test_add_student(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.post('/add_student/',
                                    {'first_name': 'mamad', 'last_name': 'rezaie', 'student_number': '92100773',
                                     'national_code': '0019154122'})
        self.assertIs(response.status_code, 200)

    def test_add_prof_form(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get("add_prof/")
        self.assertIs(response.status_code, 200)

    def test_add_prof(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.post('/add_prof/',
                                    {'first_name': 'mamad', 'last_name': 'rezaie'})
        self.assertIs(response.status_code, 200)

    def test_add_course_form(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get("add_course/")
        self.assertIs(response.status_code, 200)

    def test_add_course(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.post('/add_course/',
                                    {'name': 'riazi', 'prof': 'Kasra Alishahi', 'students': 'mamad rezaie, reza bani'})
        self.assertIs(response.status_code, 200)

    def test_delete_student(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/delete_student/',
                                   {'id': '1'})
        self.assertIs(response.status_code, 200)

    def test_delete_prof(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/delete_prof/',
                                   {'id': '1'})
        self.assertIs(response.status_code, 200)

    def test_delete_course(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/delete_course/',
                                   {'id': '1'})
        self.assertIs(response.status_code, 200)

    def test_list_students(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/students/', {})
        self.assertIs(response.status_code, 200)

    def test_list_profs(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/profs/', {})
        self.assertIs(response.status_code, 200)

    def test_list_courses(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/courses/', {})
        self.assertIs(response.status_code, 200)

    def test_list_questions(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/questions/', {})
        self.assertIs(response.status_code, 200)

    def test_list_exams(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/exams/', {})
        self.assertIs(response.status_code, 200)

    def test_add_question_form(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/add_prof/')
        self.assertIs(response.status_code, 200)

    def test_add_exam_form(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/add_exam/')
        self.assertIs(response.status_code, 200)

    def test_show_exam(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/show_exam/')
        self.assertIs(response.status_code, 200)

    def test_delete_question(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/delete_question/',
                                   {'id': '1'})
        self.assertIs(response.status_code, 200)

    def test_delete_exam(self):
        self.client = Client(enforce_csrf_checks=False)
        response = self.client.get('/delete_exam/',
                                   {'id': '1'})
        self.assertIs(response.status_code, 200)