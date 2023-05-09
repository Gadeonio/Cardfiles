from django.views.generic import ListView

from cardfile.filters import *
from cardfile.models import Genre, Composer, AuthorOfText, Performer, Artwork, Performance, Record
from cardfile.views.common_mixins import NavMixin, FiltersMixin


class TemplateNameSuffixMixin:
    template_name_suffix: str = ""


class MainMixin(NavMixin, TemplateNameSuffixMixin, FiltersMixin):
    pass


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
