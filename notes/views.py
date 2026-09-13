import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .data import NOTES, TAGS, THEMES, FONTS
from .forms import NoteForm


def _get_settings(request):
    theme = request.COOKIES.get("theme", "light")
    font_size = int(request.COOKIES.get("font_size", 16))
    if theme not in THEMES:
        theme = 'light'
    if font_size not in FONTS:
        font_size = 16

    return theme, font_size


def index(request):
    theme, font_size = _get_settings(request)
    return render(request, 
                  "notes/index.html", {
                      "notes": NOTES,
                      "theme": theme,
                      "theme_info": THEMES[theme],
                      "font_size": font_size,
                      "themes": THEMES,
                      "fonts": FONTS
                  }
                )


def note_detail(request, note_id):
    theme, font_size = _get_settings(request)
    note = next((n for n in NOTES if n['id'] == note_id), None)
    if note is None:
        return HttpResponse("Заметка не найдена", status=404)

    return render(request, 
                  "notes/note_data.html", {
                      "note": note,
                      "theme": theme,
                      "theme_info": THEMES[theme],
                      "font_size": font_size
                  })


def settings_view(request):
    theme, font_size = _get_settings(request)

    if request.method == "POST":
        new_theme = request.POST.get("theme", "light")
        new_font = int(request.POST.get("font_size", 16))
        response = redirect("settings")

        response.set_cookie("theme", new_theme, max_age=60*60*24*30)
        response.set_cookie("font_size", str(new_font), max_age=60*60*24*30)


        return response

    return render(request,
                  "notes/settings.html", {
                      "current_theme": theme,
                      "current_font": font_size,
                      "theme_info": THEMES[theme],
                      "font_size": font_size,
                      "themes": THEMES,
                      "fonts": FONTS
                  })


def add_note(request):
    theme, font_size = _get_settings(request)

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_id = str(uuid.uuid4())
            new_note = {
                "id": new_id,
                "title": form.cleaned_data['title'],
                "text": form.cleaned_data['text'],
                "tag": form.cleaned_data['tag']
            }

            NOTES.append(new_note)

            return redirect('index')

    else:
        form = NoteForm()

    return render(request,
                  "notes/add_note.html", {
                      "form": form,
                      "theme": theme,
                      "theme_info": THEMES[theme],
                      "font_size": font_size
                  })


def delete_note(request, note_id):
    if request.method == "POST":
        note_to_delete = next((n for n in NOTES if n['id'] == note_id), None)

        if note_to_delete:
            NOTES.remove(note_to_delete)
        return redirect('index')

    theme, font_size = _get_settings(request)
    note = next((n for n in NOTES if n['id'] == note_id), None)
    
    if note is None:
        return HttpResponse("Заметка не найдена", status=404)
    
    return render(request, "notes/delete_confirm.html", {
        "note": note,
        "theme": theme,
        "theme_info": THEMES[theme],
        "font_size": font_size
    })