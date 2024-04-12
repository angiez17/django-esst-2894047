from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView
from . models import Notes
from .forms import NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

