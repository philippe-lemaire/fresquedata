from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Card

# Create your views here.


class IndexView(TemplateView):
    template_name = "cardfactory/index.html"


class CardListView(ListView):
    template_name = "cardfactory/card_list.html"
    model = Card
    context_object_name = "card_list"
