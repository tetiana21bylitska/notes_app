import pytest
from ..forms import NoteForm
from .factories import CategoryFactory

@pytest.mark.django_db
class TestNoteForm:

    def test_note_form_valid(self):
        category = CategoryFactory()
        form_data = {
            'title': 'Valid Title',
            'text': 'Some content',
            'category': category.id
        }
        form = NoteForm(data=form_data)
        assert form.is_valid()

    def test_note_form_missing_required_fields(self):
        form = NoteForm(data={})
        assert not form.is_valid()
        assert 'title' in form.errors
        assert 'text' in form.errors
        assert 'category' in form.errors

    def test_note_form_optional_reminder(self):
        category = CategoryFactory()
        form_data = {
            'title': 'Task',
            'text': 'Details',
            'category': category.id,
            'reminder': ''
        }
        form = NoteForm(data=form_data)
        assert form.is_valid()

    def test_note_form_invalid_category(self):
        form_data = {
            'title': 'Title',
            'text': 'Text',
            'category': 9999
        }
        form = NoteForm(data=form_data)
        assert not form.is_valid()
        assert 'category' in form.errors