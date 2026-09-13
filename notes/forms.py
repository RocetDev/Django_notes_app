from django import forms
from .data import TAGS

class NoteForm(forms.Form):
    title = forms.CharField(
        label="Заголовок",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "from-control"})
    )

    text = forms.CharField(
        label="Текст Заметки",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )

    tag = forms.ChoiceField(
        label="Тег",
        choices=[(t, t) for t in TAGS],
        widget=forms.Select(attrs={"class": "form-control"})
    )