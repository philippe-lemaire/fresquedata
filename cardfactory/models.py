from django.db import models
from tinymce.models import HTMLField
from file_validator.models import DjangoFileValidator


# Create your models here.
class Card(models.Model):
    title = models.TextField("Titre", max_length=200, unique=True)
    batch = models.IntegerField("Numéro de Lot", default=1)
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
        "Note sur l'illustration", max_length=300, blank=True
    )
    content = HTMLField("Verso de la carte", max_length=1000, blank=True)
