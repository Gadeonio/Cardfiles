import django_filters
import cardfile.models


class ComposerFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Composer
        fields = "__all__"


class GenreFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Genre
        fields = "__all__"


class AuthorOfTextFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.AuthorOfText
        fields = "__all__"


class PerformerFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Performer
        fields = "__all__"


class ArtworkFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Artwork
        fields = "__all__"


class PerformanceFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Performance
        fields = "__all__"


class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = cardfile.models.Record
        fields = "__all__"
