from django import forms
import cardfile.models



class ComposerEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Composer
        fields = "__all__"


class GenreEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Genre
        fields = "__all__"


class AuthorOfTextEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.AuthorOfText
        fields = "__all__"


class PerformerEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Performer
        fields = "__all__"


class ArtworkEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Artwork
        fields = "__all__"


class PerformanceEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Performance
        fields = "__all__"


class RecordEdit(forms.ModelForm):
    class Meta:
        model = cardfile.models.Record
        fields = "__all__"

