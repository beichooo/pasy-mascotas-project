from django import forms
from .models import Pets, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "shelter_name",
            "shelter_logo",
            "shelter_description",
            "link_whatsapp",
            "link_facebook",
            "link_tiktok",
            "link_instagram",
            "qr_donation",
            "address",
            "link_maps",
        )


class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        exclude = ["user"]
