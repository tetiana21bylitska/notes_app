import pytest
from .factories import NoteFactory, UserFactory, CategoryFactory
from ..models import Note, Category


@pytest.mark.django_db
class TestCategoryModel:

    def test_category_crud(self):
        category = CategoryFactory(title="Work")
        assert str(category) == "Work"

        category.title = "Personal"
        category.save()
        assert Category.objects.get(id=category.id).title == "Personal"

        category_id = category.id
        category.delete()
        assert not Category.objects.filter(id=category_id).exists()


@pytest.mark.django_db
class TestNoteModel:
    def test_note_creation_and_read(self, note):
        assert note.id is not None
        assert isinstance(note.title, str)
        assert note.get_absolute_url() == f"/{note.pk}/"

    def test_note_update(self):
        note = NoteFactory(title="Old Title")
        note.title = "New Title"
        note.save()
        assert Note.objects.get(id=note.id).title == "New Title"

    def test_note_delete(self):
        note = NoteFactory()
        note_id = note.id
        note.delete()
        assert not Note.objects.filter(id=note_id).exists()

    def test_note_author_relationship(self):
        user = UserFactory(username="Ivan")
        NoteFactory(author=user)
        assert user.notes.count() == 1

    def test_note_cascade_delete_with_user(self, user, category):
        NoteFactory(author=user, category=category)
        user.delete()
        assert Note.objects.filter(author_id=user.id).count() == 0


@pytest.mark.django_db
def test_category_cascade_delete(category):
    Note.objects.create(title="Тимчасова", text="Буде видалена", category=category)
    assert Note.objects.filter(category=category).count() == 1

    category.delete()
    assert Note.objects.filter(title="Тимчасова").count() == 0