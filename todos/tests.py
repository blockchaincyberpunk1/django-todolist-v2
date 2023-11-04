from django.test import TestCase
from .models import TodoItem

class TodoItemTestCase(TestCase):
    def test_create_todo_item(self):
        task = TodoItem.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

    def test_complete_todo_item(self):
        task = TodoItem.objects.create(title="Incomplete Task")
        task.completed = True
        task.save()
        self.assertTrue(task.completed)

    def test_delete_todo_item(self):
        task = TodoItem.objects.create(title="Task to Delete")
        task.delete()
        self.assertEqual(TodoItem.objects.count(), 0)

 