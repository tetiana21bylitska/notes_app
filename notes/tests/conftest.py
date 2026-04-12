import pytest
from .factories import NoteFactory, CategoryFactory, UserFactory

@pytest.fixture
def user(db):
    return UserFactory()

@pytest.fixture
def category(db):
    return CategoryFactory()

@pytest.fixture
def note(db, category, user):
    return NoteFactory(category=category, author=user)