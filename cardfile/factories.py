import factory
from factory import Factory, SubFactory
from factory.django import DjangoModelFactory
from cardfile.models import *


class ComposerFactory(DjangoModelFactory):
    class Meta:
        model = Composer

    name = factory.Faker('name')


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = 'Classic'


class AuthorOfTextFactory(DjangoModelFactory):
    class Meta:
        model = AuthorOfText

    name = factory.Faker('name')


class PerformerFactory(DjangoModelFactory):
    class Meta:
        model = Performer

    name = factory.Faker('name')


class ArtworkFactory(DjangoModelFactory):
    class Meta:
        model = Artwork

    name = factory.Faker('word')

    @factory.post_generation
    def composers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for composer in extracted:
                self.composers.add(ComposerFactory())


    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genres.add(GenreFactory())

    @factory.post_generation
    def authors_of_text(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author_of_text in extracted:
                self.authors_of_text.add(AuthorOfTextFactory())


class PerformanceFactory(DjangoModelFactory):
    class Meta:
        model = Performance

    artworks = SubFactory(ArtworkFactory)

    @factory.post_generation
    def performers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for performer in extracted:
                self.performers.add(PerformerFactory())


class RecordFactory(DjangoModelFactory):
    class Meta:
        model = Record

    name = factory.Faker('word')

    @factory.post_generation
    def performances(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for performance in extracted:
                self.performances.add(PerformanceFactory())
