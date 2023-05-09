from django.db import models
from django.views.generic import DetailView

from cardfile.models import *


def get_template_name(name):
    return 'cardfile/details/' + name + '_detail' + '.html'


class DetailMixin(DetailView):
    name = ''
    template_name = get_template_name(name)


class ComposerDetail(DetailMixin):
    queryset = Composer.objects.all()
    name = 'composer'
    template_name = get_template_name(name)


class GenreDetail(DetailMixin):
    queryset = Genre.objects.all()
    name = 'genre'
    template_name = get_template_name(name)


class AuthorOfTextDetail(DetailMixin):
    queryset = AuthorOfText.objects.all()

    name = 'author_of_text'
    template_name = get_template_name(name)


class PerformerDetail(DetailMixin):
    queryset = Performer.objects.all()
    name = 'performer'
    template_name = get_template_name(name)


class ArtworkDetail(DetailMixin):
    queryset = Artwork.objects.all()
    name = 'artwork'
    template_name = get_template_name(name)


class PerformanceDetail(DetailMixin):
    queryset = Performance.objects.all()
    name = 'performance'
    template_name = get_template_name(name)


class RecordDetail(DetailMixin):
    queryset = Record.objects.all()
    name = 'record'
    template_name = get_template_name(name)

