from django.contrib import admin
from django.urls import path

from cardfile.views import ComposerView, RecordView, GenreView, ArtworkView, PerformerView, PerformanceView, \
    AuthorOfTextView, BaseView

app_name = "cardfile"

urlpatterns = [
    path('', BaseView.as_view(), name="base"),
    path('composer/', ComposerView.as_view(), name="composer"),
    path('record/', RecordView.as_view(), name="record"),
    path('genre/', GenreView.as_view(), name="genre"),
    path('artwork/', ArtworkView.as_view(), name="artwork"),
    path('performer/', PerformerView.as_view(), name="performer"),
    path('performance/', PerformanceView.as_view(), name="performance"),
    path('author_of_text/', AuthorOfTextView.as_view(), name="author_of_text"),
]
