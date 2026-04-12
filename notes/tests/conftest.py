import pytest
from .factories import NoteFactory, CategoryFactory

@pytest.fixture
def category(db):
    return CategoryFactory()

@pytest.fixture
def note(db, category):
    return NoteFactory(category=category)