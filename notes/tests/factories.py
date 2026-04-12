import factory
from django.contrib.auth.models import User
from notes.models import Note, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    title = factory.Faker('word')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')

class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Faker('sentence', nb_words=3)
    text = factory.Faker('paragraph')
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)