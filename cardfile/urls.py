from django.contrib import admin
from django.urls import path

from cardfile.views.details import ComposerDetail, GenreDetail, RecordDetail, ArtworkDetail, PerformerDetail, \
    PerformanceDetail, AuthorOfTextDetail
from cardfile.views.lists import ComposerView, RecordView, GenreView, ArtworkView, PerformerView, PerformanceView, \
    AuthorOfTextView
from cardfile.views.other import BaseView

from cardfile.views.creates import ComposerCreate, RecordCreate, GenreCreate, ArtworkCreate, PerformerCreate, \
    PerformanceCreate, AuthorOfTextCreate

from cardfile.views.deletes import *
from cardfile.views.updates import *

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

    path('composer/create', ComposerCreate.as_view(), name="composer_create"),
    path('record/create', RecordCreate.as_view(), name="record_create"),
    path('genre/create', GenreCreate.as_view(), name="genre_create"),
    path('artwork/create', ArtworkCreate.as_view(), name="artwork_create"),
    path('performer/create', PerformerCreate.as_view(), name="performer_create"),
    path('performance/create', PerformanceCreate.as_view(), name="performance_create"),
    path('author_of_text/create', AuthorOfTextCreate.as_view(), name="author_of_text_create"),

    path('composer/<int:pk>', ComposerDetail.as_view(), name="composer_detail"),
    path('record/<int:pk>', RecordDetail.as_view(), name="record_detail"),
    path('genre/<int:pk>', GenreDetail.as_view(), name="genre_detail"),
    path('artwork/<int:pk>', ArtworkDetail.as_view(), name="artwork_detail"),
    path('performer/<int:pk>', PerformerDetail.as_view(), name="performer_detail"),
    path('performance/<int:pk>', PerformanceDetail.as_view(), name="performance_detail"),
    path('author_of_text/<int:pk>', AuthorOfTextDetail.as_view(), name="author_of_text_detail"),

    path('composer/<int:pk>/delete', ComposerDelete.as_view(), name="composer_delete"),
    path('record/<int:pk>/delete', RecordDelete.as_view(), name="record_delete"),
    path('genre/<int:pk>/delete', GenreDelete.as_view(), name="genre_delete"),
    path('artwork/<int:pk>/delete', ArtworkDelete.as_view(), name="artwork_delete"),
    path('performer/<int:pk>/delete', PerformerDelete.as_view(), name="performer_delete"),
    path('performance/<int:pk>/delete', PerformanceDelete.as_view(), name="performance_delete"),
    path('author_of_text/<int:pk>/delete', AuthorOfTextDelete.as_view(), name="author_of_text_delete"),

    path('composer/<int:pk>/update', ComposerUpdate.as_view(), name="composer_update"),
    path('record/<int:pk>/update', RecordUpdate.as_view(), name="record_update"),
    path('genre/<int:pk>/update', GenreUpdate.as_view(), name="genre_update"),
    path('artwork/<int:pk>/update', ArtworkUpdate.as_view(), name="artwork_update"),
    path('performer/<int:pk>/update', PerformerUpdate.as_view(), name="performer_update"),
    path('performance/<int:pk>/update', PerformanceUpdate.as_view(), name="performance_update"),
    path('author_of_text/<int:pk>/update', AuthorOfTextUpdate.as_view(), name="author_of_text_update"),

]
