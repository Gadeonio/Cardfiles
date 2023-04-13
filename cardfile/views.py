from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cardfile.models import Genre,Composer,AuthorOfText,Performer,Artwork,Performance,Record


class GenreView(ListView):
    model = Genre


class ComposerView(ListView):
    model = Composer


class AuthorOfTextView(ListView):
    model = AuthorOfText


class PerformerView(ListView):
    model = Performer


class ArtworkView(ListView):
    model = Artwork


class PerformanceView(ListView):
    model = Performance


class RecordView(ListView):
    model = Record

