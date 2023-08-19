# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("donaciones/", views.donation_home, name="donations"),
    path("albergue/<int:shelter_id>/", views.shelter_profile, name="shelter_profile"),
]
