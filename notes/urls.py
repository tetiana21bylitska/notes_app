from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('create/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('import/sync/', SyncNoteImportView.as_view(), name='sync_import'),
    path('import/async/', AsyncNoteImportView.as_view(), name='async_import'),
    path('import/comparison/', HttpClientComparisonView.as_view(), name='http_comparison'),
]