from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from cardfile.models import Genre,Composer,AuthorOfText,Performer,Artwork,Performance,Record


'''class NothingMixin:
    nothing = "Nothing"


class NaitonMixin:
    name = "Naiton"


class DethklokMixin(NothingMixin, NaitonMixin):
    pass


class MetallocalypsMixin(DethklokMixin):
    pass

'''
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


class MainMixin(NavMixin, TemplateNameSuffixMixin):
    pass


class BaseView(MainMixin, TemplateView):
    template_name = "cardfile/base.html"


class GenreView(MainMixin, ListView):
    model = Genre


class ComposerView(MainMixin, ListView):
    model = Composer


class AuthorOfTextView(MainMixin, ListView):
    model = AuthorOfText
    template_name = 'cardfile/author_of_text.html'


class PerformerView(MainMixin, ListView):
    model = Performer


class ArtworkView(MainMixin, ListView):
    model = Artwork


class PerformanceView(MainMixin, ListView):
    model = Performance


class RecordView(MainMixin, ListView):
    model = Record

