from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.


class CustomUser(AbstractUser):
    shelter_name = models.CharField(max_length=50)
    shelter_logo = models.ImageField(upload_to="qr_donations/")
    shelter_description = models.TextField(max_length=250)
    link_whatsapp = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_tiktok = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    qr_donation = models.ImageField(upload_to="shelter_logos/")
    address = models.TextField(max_length=250)
    link_maps = models.URLField(blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Custom Users"


# TODO: I dont use the multifield upload, instead use two single image upload, fix in the future
class Pets(models.Model):
    SPECIES_CHOICES = (("Perro", "Perro"), ("Gato", "Gato"))

    GENDER_CHOICES = (
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
    )

    SIZE_CHOICES = (
        ("Pequeño", "Pequeño"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    )

    HEALTH_CHOICES = (
        ("Saludable", "Saludable"),
        ("Necesita tratamiento", "Necesita tratamiento"),
        ("En tratamiento", "En tratamiento"),
    )

    PERSONALITY_CHOICES = (
        ("Amigable", "Amigable"),
        ("Juguetón", "Juguetón"),
        ("Tranquilo", "Tranquilo"),
        ("Atención", "Atención"),
        ("Tímido", "Tímido"),
    )

    name = models.CharField(max_length=50)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    health = models.CharField(max_length=20, choices=HEALTH_CHOICES)
    health_detail = models.TextField(max_length=350)
    personality = models.CharField(max_length=20, choices=PERSONALITY_CHOICES)
    pers_detail = models.TextField(max_length=350)
    photos = models.ImageField(upload_to="pet_photos/")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="pets")

    def __str__(self):
        return f"{self.name} ({self.species})"

    def delete(self):
        self.photos.delete()
        super().delete()

    class Meta:
        verbose_name_plural = "Pets"
