from django.urls import reverse
from django.views.generic import DeleteView

import cardfile.models


def get_template_name(name):
    return 'cardfile/deletes/' + name + '_delete' + '.html'


class DeleteMixin(DeleteView):
    name = ''
    template_name = get_template_name(name)

    def get_success_url(self):
        return reverse(f"cardfile:{self.name}")


class ComposerDelete(DeleteMixin):
    name = 'composer'
    model = cardfile.models.Composer
    template_name = get_template_name(name)


class GenreDelete(DeleteMixin):
    name = 'genre'
    model = cardfile.models.Genre
    template_name = get_template_name(name)


class AuthorOfTextDelete(DeleteMixin):
    name = 'author_of_text'
    model = cardfile.models.AuthorOfText
    template_name = get_template_name(name)


class PerformerDelete(DeleteMixin):
    name = 'performer'
    model = cardfile.models.Performer
    template_name = get_template_name(name)


class ArtworkDelete(DeleteMixin):
    name = 'artwork'
    model = cardfile.models.Artwork
    template_name = get_template_name(name)


class PerformanceDelete(DeleteMixin):
    name = 'performance'
    model = cardfile.models.Performance
    template_name = get_template_name(name)


class RecordDelete(DeleteMixin):
    name = 'record'
    model = cardfile.models.Record
    template_name = get_template_name(name)
