from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registrar/", views.sign_up, name="sign_up"),
    path("cerrar-sesion/", views.sign_out, name="sign_out"),
    # the accounts/login. is a default path for the @login decorator
    path("accounts/login/", views.sign_in, name="sign_in"),
    path("mascotas/", views.pet_list, name="pet_list"),
    path("mascotas/agregar/", views.add_pet, name="add_pet"),
    path("mascotas/editar/<int:pet_id>/", views.edit_pet, name="edit_pet"),
    path("mascotas/editar/eliminar/<int:pk>/", views.delete_pet, name="delete_pet"),
]
