from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тип справи")

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Що зробити")
    text = models.TextField(verbose_name="Деталі завдання")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Коли виконати")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    remind_at = models.DateTimeField(null=True, blank=True, verbose_name="Коли нагадати?")
    is_sent = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', verbose_name="Автор", null=True, blank=True)
    group = models.ForeignKey('auth.Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']