from django.test import TestCase
from .models import Notes
from .forms import NotesForm

class NotesFormTest(TestCase):
    def add_note(self,title="Bills", text="water"):
        return Notes.object.create(title=title, text=text)

