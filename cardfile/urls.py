from django.contrib import admin
from django.urls import path

from cardfile.views import ComposerView, RecordView, GenreView, ArtworkView, PerformerView, PerformanceView, AuthorOfTextView

appname = "cardfile"

urlpatterns = [
    path('/', ComposerView.as_view()),
    path('composer/', ComposerView.as_view()),
    path('record/', RecordView.as_view()),
    path('genre/', GenreView.as_view()),
    path('artwork/', ArtworkView.as_view()),
    path('performer/', PerformerView.as_view()),
    path('performance/', PerformanceView.as_view()),
    path('author_of_text/', AuthorOfTextView.as_view()),
]
