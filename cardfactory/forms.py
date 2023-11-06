from django import forms
from .models import Card
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ("pk",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.add_input(
            Submit(
                "submit",
                "Modifier Carte",
                css_class="m-1 btn-secondary",
            )
        )
