from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("note/<str:note_id>/", views.note_detail, name="note_detail"),
    path("settings/", views.settings_view, name="settings"),
    path("add/", views.add_note, name="add_note"),
    path("note/<str:note_id>/delete/", views.delete_note, name="delete_note"),
]