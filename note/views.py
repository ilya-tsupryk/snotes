from django.http import HttpResponse
from django.shortcuts import render

from note.models import Note


def notes_view(request):
    notes = Note.objects.all()
    return HttpResponse(notes)