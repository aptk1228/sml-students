from django.test import TestCase, Client
from base.models import Student


class TestStudentList(TestCase):
    def test_student_list_correct(self):
        client = Client()
        response = client.get("/api/students/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), Student.objects.count())


class TestStudentCreation(TestCase):
    def test_student_creation_correct(self):
        client = Client()
        response = client.post(
            "/api/students/",
            content_type="application/json",
            data={
                "full_name": "Иванов Иван Иванович",
                "birth_date": "01-01-1990",
                "mark": 2
            })
        self.assertEqual(response.status_code, 201)
        student = Student.objects.get(id=response.json()["id"])
        self.assertEqual(student.full_name, "Иванов Иван Иванович")
        self.assertEqual(student.birth_date.strftime("%d-%m-%Y"), "01-01-1990")
        self.assertEqual(student.mark, 2)

    def test_student_creation_wrong_content_type(self):
        client = Client()
        response = client.post(
            "/api/students/",
            content_type="text/plain",
            data={
                "full_name": "Иванов Иван Иванович",
                "birth_date": "01-01-1990",
                "mark": 2
            })
        self.assertEqual(response.status_code, 415)

    def test_student_creation_wrong_structure(self):
        client = Client()
        response = client.post(
            "/api/students/",
            content_type="application/json",
            data={
                "student": {
                    "full_name": "Иванов Иван Иванович",
                    "birth_date": "01-01-1990",
                    "mark": 2
                }
            })
        self.assertEqual(response.status_code, 400)


class TestStudentUpdate(TestCase):
    def init_student(self):
        student, created = Student.objects.get_or_create(
            full_name="Петров Петр Петрович", birth_date="1990-01-01", mark=2)
        return student

    def test_student_update_name(self):
        student = self.init_student()
        client = Client()
        response = client.patch(
            "/api/students/{}".format(student.pk),
            content_type="application/json",
            data={
                "full_name": "Кузнецов Петр Петрович"
            })
        self.assertEqual(response.status_code, 200)
        student.refresh_from_db()
        self.assertEqual(student.full_name, "Кузнецов Петр Петрович")

    def test_student_update_birth_date(self):
        student = self.init_student()
        client = Client()
        response = client.patch(
            "/api/students/{}".format(student.pk),
            content_type="application/json",
            data={
                "birth_date": "01-01-1991"
            })
        self.assertEqual(response.status_code, 200)
        student.refresh_from_db()
        self.assertEqual(student.birth_date.strftime("%d-%m-%Y"), "01-01-1991")

    def test_student_update_mark(self):
        student = self.init_student()
        client = Client()
        response = client.patch(
            "/api/students/{}".format(student.pk),
            content_type="application/json",
            data={
                "mark": 4
            })
        self.assertEqual(response.status_code, 200)
        student.refresh_from_db()
        self.assertEqual(student.mark, 4)

    def test_student_update_all_fields(self):
        student = self.init_student()
        client = Client()
        response = client.patch(
            "/api/students/{}".format(student.pk),
            content_type="application/json",
            data={
                "full_name": "Кузнецов Петр Петрович",
                "birth_date": "01-01-1991",
                "mark": 4
            })
        self.assertEqual(response.status_code, 200)
        student.refresh_from_db()
        self.assertEqual(student.full_name, "Кузнецов Петр Петрович")
        self.assertEqual(student.birth_date.strftime("%d-%m-%Y"), "01-01-1991")
        self.assertEqual(student.mark, 4)

    def test_student_update_404(self):
        client = Client()
        response = client.put(
            "/api/students/999999",
            content_type="application/json",
            data={
                "student": {
                    "full_name": "Кузнецов Петр Петрович",
                    "birth_date": "01-01-1991",
                    "mark": 4
                }
            })
        self.assertEqual(response.status_code, 404)


class TestStudentDeletion(TestCase):
    def init_student(self):
        student, created = Student.objects.get_or_create(
            full_name="Петров Петр Петрович", birth_date="1990-01-01", mark=2)
        return student

    def test_student_deletion_correct(self):
        student = self.init_student()
        client = Client()
        response = client.delete("/api/students/{}".format(student.pk))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())

    def test_student_deletion_404(self):
        client = Client()
        response = client.delete("/api/students/999999")
        self.assertEqual(response.status_code, 404)


class TestStudentModel(TestCase):
    def init_student(self):
        student, created = Student.objects.get_or_create(
            full_name="Петров Петр Петрович", birth_date="1990-01-01", mark=2)
        return student

    def test_student_creation(self):
        student = self.init_student()
        self.assertIsInstance(student, Student)
        self.assertEqual(student.__str__(), student.full_name)
