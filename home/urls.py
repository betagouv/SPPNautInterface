"""
Router config for home module
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.tableau_redirect),
    path(
        "tableau/",
        views.tableau,
        name="tableau",
    ),
    path(
        "publication/",
        views.publication_upload,
        name="publication_upload",
    ),
    path("publication/<slug:generation_id>/", views.publication_display, name="publication_display"),
]
