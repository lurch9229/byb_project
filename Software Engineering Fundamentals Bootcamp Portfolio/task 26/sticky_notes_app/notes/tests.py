import os
import django
from django.test import TestCase, Client
from notes.models import StickyNote
from notes.forms import StickyNoteForm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
django.setup()


class StickyNoteModelTest(TestCase):

    def setUp(self):
        # Create a sample StickyNote instance
        self.note = StickyNote.objects.create(
            title="Test Note",
            description="This is a test note.",
            is_visible=True
        )

    def test_string_representation(self):
        # Test the string representation of the StickyNote instance
        self.assertEqual(str(self.note), self.note.title)

    def test_note_creation(self):
        # Test that the StickyNote instance is created correctly
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.description, "This is a test note.")
        self.assertTrue(self.note.is_visible)

    def test_default_is_visible(self):
        # Test the default value of is_visible
        note = StickyNote.objects.create(
            title="Another Test Note",
            description="Another test description."
        )
        self.assertTrue(note.is_visible)

    def test_date_added_auto_now(self):
        # Test that date_added is set automatically
        self.assertIsNotNone(self.note.date_added)


class StickyNoteFormTest(TestCase):

    def test_form_fields(self):
        # Test that the form has the correct fields
        form = StickyNoteForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)

    def test_form_valid_data(self):
        # Test form with valid data
        form_data = {
            'title': 'Test Note',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        # Test form with invalid data (missing title)
        form_data = {
            'title': '',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_save(self):
        # Test saving the form
        form_data = {
            'title': 'Test Note',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertTrue(form.is_valid())
        note = form.save()
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.description, 'This is a test description.')


class StickyNoteFormTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.note = StickyNote.objects.create(
            title="Test Note",
            description="This is a test note.",
            is_visible=True
        )

    def test_form_fields(self):
        form = StickyNoteForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)

    def test_form_valid_data(self):
        form_data = {
            'title': 'Test Note',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'title': '',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_save(self):
        form_data = {
            'title': 'Test Note',
            'description': 'This is a test description.'
        }
        form = StickyNoteForm(data=form_data)
        self.assertTrue(form.is_valid())
        note = form.save()
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.description, 'This is a test description.')
