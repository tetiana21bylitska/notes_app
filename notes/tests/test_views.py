import pytest
from django.urls import reverse
from notes.models import Note, Category
from .factories import NoteFactory, CategoryFactory


@pytest.mark.django_db
def test_note_list_view(client, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='password')
    client.force_login(user)

    url = reverse('note_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_note_create_view(client, django_user_model):
    category = CategoryFactory()
    user = django_user_model.objects.create_user(username='tanya_test', password='password123')
    client.force_login(user)

    url = reverse('note_create')


    data = {
        'title': 'Купити квіти',
        'text': 'Треба замовити півонії на завтра',
        'category': category.id,
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert Note.objects.filter(title='Купити квіти').exists()

    new_note = Note.objects.get(title='Купити квіти')
    assert new_note.text == 'Треба замовити півонії на завтра'


@pytest.mark.django_db
def test_note_detail_view(client, django_user_model):
    user = django_user_model.objects.create_user(username='tanya', password='123')

    client.force_login(user)
    note = NoteFactory(author=user)
    url = reverse('note_detail', kwargs={'pk': note.pk})
    response = client.get(url)

    assert response.status_code == 200