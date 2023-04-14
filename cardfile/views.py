from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from cardfile.models import Genre,Composer,AuthorOfText,Performer,Artwork,Performance,Record


class TemplateNameSuffixMixin:
    template_name_suffix: str = ""


class NavMixin:
    navs = {'cardfile:base': 'Базовая страница',
            'cardfile:composer': 'Композиторы',
            'cardfile:record': 'Пластинки',
            'cardfile:genre': 'Жанры',
            'cardfile:artwork': 'Произведения',
            'cardfile:performer': 'Исполнители',
            'cardfile:performance': 'Исполнения',
            'cardfile:author_of_text': 'Авторы текста'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['nav_names'] = self.get_nav_names()
        return context

    def get_nav_names(self):
        return self.navs


class BaseView(NavMixin, TemplateNameSuffixMixin, TemplateView):
    template_name = "cardfile/base.html"


class GenreView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Genre


class ComposerView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Composer


class AuthorOfTextView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = AuthorOfText
    template_name = 'cardfile/author_of_text.html'


class PerformerView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Performer


class ArtworkView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Artwork


class PerformanceView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Performance


class RecordView(NavMixin, TemplateNameSuffixMixin, ListView):
    model = Record

