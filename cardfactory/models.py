from django.db import models
from tinymce.models import HTMLField
from file_validator.models import DjangoFileValidator


# Create your models here.
class Card(models.Model):
    title = models.CharField("Titre", max_length=200, unique=True)
    batch = models.IntegerField("Numéro de Lot", default=1)
    card_number = models.IntegerField(
        "Numéro de carte dans le lot", blank=True, default=1
    )
    illustration = models.ImageField(
        blank=True,
        upload_to="photos/",
        validators=[
            DjangoFileValidator(
                libraries=[
                    "python_magic",
                    "filetype",
                ],  # => validation operations will be performed with python-magic and filetype libraries
                acceptable_mimes=[
                    "image/png",
                    "image/jpeg",
                    "image/jpg",
                    "image/webp",
                ],  # => The mimes you want the file to be checked based on.
                acceptable_types=["image"],
                max_upload_file_size=5242880,
            )
        ],  # => 5 MB
    )
    illustation_footnote = models.CharField(
        "Note sur l'illustration", max_length=500, blank=True
    )
    content = HTMLField("Verso de la carte", max_length=10000, blank=True)

    def __str__(self):
        return f"Lot {self.batch} : {self.title}"
