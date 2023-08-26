from django.shortcuts import render
from manage_pets.models import CustomUser

# Create your views here.


def index(request):
    return render(request, "index.html")


def donation_home(request):
    shelters = CustomUser.objects.all().exclude(username="beichooo")
    return render(request, "donations.html", {"shelters": shelters})


def shelter_profile(request, shelter_id):
    shelter = CustomUser.objects.get(pk=shelter_id)
    if request.method == "GET":
        return render(request, "donations_shelter.html", {"shelter": shelter})
    else:
        return render(request, "search_results.html")


def info_adopt(request):
    return render(request, "info_adopt.html")
