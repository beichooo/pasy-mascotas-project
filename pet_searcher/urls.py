from django.urls import path
from . import views

urlpatterns = [
    # path("", views.hello, name="inicio_buscador"),
    path("", views.search_form_page, name="search_form"),
    path("buscar/", views.search_pets, name="search_pets"),
    path("info-mascota/<int:pet_id>/", views.info_pet, name="info_pet"),
    path("visita/<int:pet_id>/", views.visit_pet, name="visit_pet"),
    path("visitar-gracias/<int:pet_id>/", views.thanks_visit, name="thanks_visit"),
    path("ver-todos/", views.view_all_pets, name="view_all_pets"),
]
