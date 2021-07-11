from django.test import TestCase
from books.models import Book

# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='first todo', subtitle='a subtitle here')

    def test_title_content(self):
        todo = Book.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first todo')

    def test_body_content(self):
        todo = Book.objects.get(id=1)
        expected_object_name = f'{todo.subtitle}'
        self.assertEqual(expected_object_name, 'a subtitle here')
