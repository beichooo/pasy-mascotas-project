from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Pets
from .forms import PetsForm, CustomUserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, "home.html")


def sign_up(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("sign_in")
        else:
            # TODO: Put the error and success message
            return render(request, "sign_up.html", {"form": form})
    else:
        form = CustomUserRegistrationForm()
    return render(request, "sign_up.html", {"form": form})

    # if request.method == "GET":
    #     print("mostrar interfaz")
    #     return render(request, "sign_up.html", {"form": UserCreationForm})
    # else:
    #     if request.POST["password1"] == request.POST["password2"]:
    #         try:
    #             user = User.objects.create_user(
    #                 username=request.POST["username"],
    #                 password=request.POST["password1"],
    #             )
    #             user.save()
    #             login(request, user)
    #             return redirect("pet_list")

    #         except IntegrityError:
    #             return render(
    #                 request,
    #                 "sign_up.html",
    #                 {
    #                     "form": UserCreationForm,
    #                     "error": "El usuario ya existe",
    #                 },
    #             )
    #     return render(
    #         request,
    #         "sign_up.html",
    #         {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
    #     )


def sign_out(request):
    logout(request)
    return redirect("home")


def sign_in(request):
    if request.method == "GET":
        return render(request, "sign_in.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "sign_in.html",
                {
                    "form": AuthenticationForm,
                    "error": "El usuario y/o contraseña es incorrecto",
                },
            )
        else:
            login(request, user)
            return redirect("pet_list")


# add the gtp code for the views


@login_required
def pet_list(request):
    pets = Pets.objects.filter(user=request.user)
    return render(request, "pet_list.html", {"pets": pets})


@login_required
def add_pet(request):
    if request.method == "POST":
        form = PetsForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("pet_list")
    else:
        form = PetsForm()
    return render(request, "add_pet.html", {"form": form})


@login_required
def edit_pet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    if request.method == "POST":
        form = PetsForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetsForm(instance=pet)
    return render(request, "edit_pet.html", {"form": form, "pet": pet})


@login_required
def delete_pet(request, pk):
    dog = get_object_or_404(Pets, pk=pk)
    dog.delete()
    return redirect("pet_list")

    # pet = Pets.objects.get(pk=pet_id)
    # if request.method == "POST":
    #     # Delete photos_sec file if it exists
    #     if pet.photos_sec:
    #         photos_sec_path = pet.photos_sec.path
    #         if default_storage.exists(photos_sec_path):
    #             try:
    #                 os.remove(photos_sec_path)
    #             except Exception as e:
    #                 # Handle any exception that might occur during photo deletion
    #                 print(f"Error deleting photos_sec: {e}")

    #     # Delete the pet object from the database
    #     pet.delete()

    #     # Delete photos file (similar to what you already have)
    #     photo_path = pet.photos.path
    #     if default_storage.exists(photo_path):
    #         try:
    #             os.remove(photo_path)
    #         except Exception as e:
    #             # Handle any exception that might occur during photo deletion
    #             print(f"Error deleting photo: {e}")

    #     return redirect("pet_list")
    # else:
    #     return redirect("pet_list", {"error": "la mascota no se pudo eliminar"})


# this is the first version for the manage_pets app, the next is with frontend changes
# the next app is the pet searcher
