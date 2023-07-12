from django.test import TestCase
from .models import task
from .forms import TaskForm

class TaskFormTest(TestCase):
    def add_task(self,title="Bills", text="water"):
        return task.object.create(title=title, text=text)
