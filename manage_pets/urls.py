from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_out/", views.sign_out, name="sign_out"),
    # the accounts/login. is a default path for the @login decorator
    path("accounts/login/", views.sign_in, name="sign_in"),
    path("pets/", views.pet_list, name="pet_list"),
    path("pets/add/", views.add_pet, name="add_pet"),
    path("pets/<int:pet_id>/edit/", views.edit_pet, name="edit_pet"),
    path("pets/<int:pet_id>/edit/delete/", views.delete_pet, name="delete_pet"),
]
