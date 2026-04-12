import pytest
from ..forms import NoteForm
from .factories import CategoryFactory

@pytest.mark.django_db
def test_note_form_valid():
    category = CategoryFactory()
    form_data = {
        'title': 'Купити продукти',
        'text': 'Хліб, сир, вино',
        'category': category.id
    }
    form = NoteForm(data=form_data)
    assert form.is_valid()

def test_note_form_invalid_no_title():
    form_data = {
        'title': '',
        'text': 'Просто текст',
    }
    form = NoteForm(data=form_data)
    assert not form.is_valid()
    assert 'title' in form.errors