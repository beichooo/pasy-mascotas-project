from django.shortcuts import render, HttpResponse, redirect
from manage_pets.models import Pets
from .forms import PetSearchForm

# Create your views here.


def hello(request):
    return HttpResponse("Hello world from the searcher")


def search_form_page(request):
    form = PetSearchForm
    return render(request, "search_form.html", {"form": form})


def search_pets(request):
    if request.method == "GET":
        species = request.GET.get("species")
        gender = request.GET.get("gender")
        size = request.GET.get("size")

        pets = Pets.objects.all()
        if species:
            pets = pets.filter(species=species)
        if gender:
            pets = pets.filter(gender=gender)
        if size:
            pets = pets.filter(size=size)

        return render(
            request,
            "search_results.html",
            {
                "specie_field": species,
                "gender_field": gender,
                "size_field": size,
                "pets": pets,
            },
        )

    return render(request, "search_form.html", {"form": PetSearchForm()})


def view_all_pets(request):
    pets = Pets.objects.all()

    return render(
        request,
        "search_results.html",
        {"pets": pets},
    )


def info_pet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    if request.method == "GET":
        return render(request, "view_more.html", {"pet": pet})
    else:
        return render(request, "search_results.html")


def visit_pet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    if request.method == "GET":
        return render(request, "visit_pet.html", {"pet": pet})
    else:
        return render(request, "view_more.html")


def thanks_visit(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    if request.method == "GET":
        return render(request, "thanks_visit.html", {"pet": pet})
    else:
        print("some error")
        return render(request, "visit_pet.html")
