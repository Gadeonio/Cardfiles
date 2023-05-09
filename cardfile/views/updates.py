from django.urls import reverse
from django.views.generic import UpdateView

import cardfile.forms
import cardfile.models


class UpdateMixin(UpdateView):
    model = None
    form_class = None
    template_name = 'cardfile/confirmation_form.html'
    template_name_suffix = ''
    name = ''

    def get_success_url(self):
        return reverse(f"cardfile:{self.name}")

class ComposerUpdate(UpdateMixin):
    name = 'composer'
    model = cardfile.models.Composer
    form_class = cardfile.forms.ComposerEdit


class GenreUpdate(UpdateMixin):
    name = 'genre'
    model = cardfile.models.Genre
    form_class = cardfile.forms.GenreEdit


class AuthorOfTextUpdate(UpdateMixin):
    name = 'author_of_text'
    model = cardfile.models.AuthorOfText
    form_class = cardfile.forms.AuthorOfTextEdit


class PerformerUpdate(UpdateMixin):
    name = 'performer'
    model = cardfile.models.Performer
    form_class = cardfile.forms.PerformerEdit


class ArtworkUpdate(UpdateMixin):
    name = 'artwork'
    model = cardfile.models.Artwork
    form_class = cardfile.forms.ArtworkEdit


class PerformanceUpdate(UpdateMixin):
    name = 'performance'
    model = cardfile.models.Performance
    form_class = cardfile.forms.PerformanceEdit


class RecordUpdate(UpdateMixin):
    name = 'record'
    model = cardfile.models.Record
    form_class = cardfile.forms.RecordEdit
