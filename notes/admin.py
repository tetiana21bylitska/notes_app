from django.contrib import admin
from .models import Note, Category

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'reminder')
    list_filter = ('category', 'author')
    search_fields = ('title', 'text')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass