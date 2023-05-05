from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.db import models

from cardfile.filters import *
from cardfile.models import Genre,Composer,AuthorOfText,Performer,Artwork,Performance,Record


class TemplateNameSuffixMixin:
    template_name_suffix: str = ""


class NavMixin:
    navs = {'cardfile:base':            'Базовая страница',
            'cardfile:composer':        'Композиторы',
            'cardfile:genre':           'Жанры',
            'cardfile:author_of_text':  'Авторы текста',
            'cardfile:performer':       'Исполнители',
            'cardfile:artwork':         'Произведения',
            'cardfile:performance':     'Исполнения',
            'cardfile:record':          'Пластинки'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['nav_names'] = self.get_nav_names()
        return context

    def get_nav_names(self):
        return self.navs


class FiltersMixin:

    def get_filters(self):
        return None

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['filter'] = self.get_filters()
        return context


class MainMixin(NavMixin, TemplateNameSuffixMixin, FiltersMixin):
    pass


class BaseView(MainMixin, TemplateView):
    template_name = "cardfile/base.html"


class GenreView(MainMixin, ListView):
    model = Genre

    def get_filters(self):
        return GenreFilter(self.request.GET)


class ComposerView(MainMixin, ListView):
    model = Composer

    def get_filters(self):
        return ComposerFilter(self.request.GET)


class AuthorOfTextView(MainMixin, ListView):
    model = AuthorOfText
    template_name = 'cardfile/author_of_text.html'

    def get_filters(self):
        return AuthorOfTextFilter(self.request.GET)


class PerformerView(MainMixin, ListView):
    model = Performer

    def get_filters(self):
        return PerformerFilter(self.request.GET)


class ArtworkView(MainMixin, ListView):
    model = Artwork

    def get_filters(self):
        return ArtworkFilter(self.request.GET)


class PerformanceView(MainMixin, ListView):
    model = Performance

    def get_filters(self):
        return PerformanceFilter(self.request.GET)


class RecordView(MainMixin, ListView):
    model = Record

    def get_filters(self):
        return RecordFilter(self.request.GET)


