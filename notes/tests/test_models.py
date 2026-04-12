import pytest
from ..models import Note, Category


@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(title="Навчання")
    assert category.title == "Навчання"


@pytest.mark.django_db
def test_note_creation(category):
    note = Note.objects.create(
        title="Мій перший тест",
        text="Текст нотатки",
        category=category
    )
    assert note.id is not None
    assert note.title == "Мій перший тест"
    assert note.category == category


@pytest.mark.django_db
def test_category_cascade_delete(category):
    Note.objects.create(title="Тимчасова", text="Буде видалена", category=category)
    assert Note.objects.filter(category=category).count() == 1

    category.delete()
    assert Note.objects.filter(title="Тимчасова").count() == 0