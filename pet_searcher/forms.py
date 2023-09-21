from django import forms
from manage_pets.models import Pets


class PetSearchForm(forms.Form):
    SPECIES_CHOICES = [("", "Todos")] + list(Pets.SPECIES_CHOICES)
    GENDER_CHOICES = [("", "Todos")] + list(Pets.GENDER_CHOICES)
    SIZE_CHOICES = [("", "Todos")] + list(Pets.SIZE_CHOICES)

    species = forms.ChoiceField(choices=SPECIES_CHOICES, required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    size = forms.ChoiceField(choices=SIZE_CHOICES, required=False)
    min_age = forms.IntegerField(label="Minimum Age", required=False, min_value=0)
    max_age = forms.IntegerField(label="Maximum Age", required=False, min_value=0)
