from django.db import models
from django.db.models import CASCADE

char_max_length = 200


class Composer(models.Model):
    name = models.CharField(max_length=char_max_length)

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    name = models.CharField(max_length=char_max_length)
    def __str__(self):
        return str(self.name)


class AuthorOfText(models.Model):
    name = models.CharField(max_length=char_max_length)
    def __str__(self):
        return str(self.name)


class Performer(models.Model):
    name = models.CharField(max_length=char_max_length)
    def __str__(self):
        return str(self.name)


class Artwork(models.Model):
    name = models.CharField(max_length=char_max_length)
    composers = models.ManyToManyField('cardfile.Composer', blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    authors_of_text = models.ManyToManyField(AuthorOfText, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Performance(models.Model):
    artworks = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    performers = models.ManyToManyField(Performer)

    def __str__(self):
        return str(self.artworks)


class Record(models.Model):
    name = models.CharField(max_length=char_max_length)
    performances = models.ManyToManyField(Performance)



