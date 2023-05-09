from django.urls import reverse
from django.views.generic import CreateView

from cardfile.models import *
from cardfile.forms import *


class CreateMixin(CreateView):
    model = None
    form_class = None
    template_name = 'cardfile/confirmation_form.html'
    view = None

    def get_success_url(self):
        return reverse(self.view)


class ComposerCreate(CreateMixin):
    model = Composer
    form_class = ComposerEdit
    view = 'cardfile:composer'


class GenreCreate(CreateMixin):
    model = Genre
    form_class = GenreEdit
    view = 'cardfile:genre'


class AuthorOfTextCreate(CreateMixin):
    model = AuthorOfText
    form_class = AuthorOfTextEdit
    view = 'cardfile:author_of_text'


class PerformerCreate(CreateMixin):
    model = Performer
    form_class = PerformerEdit
    view = 'cardfile:performer'


class ArtworkCreate(CreateMixin):
    model = Artwork
    form_class = ArtworkEdit
    view = 'cardfile:artwork'


class PerformanceCreate(CreateMixin):
    model = Performance
    form_class = PerformanceEdit
    view = 'cardfile:performance'


class RecordCreate(CreateMixin):
    model = Record
    form_class = RecordEdit
    view = 'cardfile:record'



