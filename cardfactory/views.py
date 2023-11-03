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
    ordering = ["batch", "card_number", "pk"]


def batch_list(request):
    template_name = "cardfactory/batch_list.html"
    cards = Card.objects.all()
    batches = list(set([card.batch for card in cards]))
    context = {"batch_list": batches}
    return render(request, template_name, context)


def card_list_per_batch(request, batch):
    template_name = "cardfactory/card_list.html"
    queryset = Card.objects.all().filter(batch=batch)
    context = {"card_list": queryset}
    return render(request, template_name, context)
