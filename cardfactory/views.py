from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Card

# Create your views here.


class IndexView(TemplateView):
    template_name = "cardfactory/index.html"


class CardListView(LoginRequiredMixin, ListView):
    template_name = "cardfactory/card_list.html"
    model = Card
    context_object_name = "card_list"
    ordering = ["batch", "card_number", "pk"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["batches_list"] = list(
            set([card.batch for card in context.get("card_list")])
        )
        return context


class CardListCompactView(CardListView):
    template_name = "cardfactory/card_compact_list.html"


class CardDetailView(LoginRequiredMixin, DetailView):
    template_name = "cardfactory/card_detail.html"
    model = Card
    context_object_name = "card"


@login_required
def batch_list(request):
    template_name = "cardfactory/batch_list.html"
    cards = Card.objects.all()
    batches = list(set([card.batch for card in cards]))
    context = {"batch_list": batches}
    return render(request, template_name, context)


@login_required
def card_list_per_batch(request, batch):
    template_name = "cardfactory/card_list.html"
    all_cards = Card.objects.all()
    queryset = all_cards.filter(batch=batch).order_by("card_number", "pk")
    batches = list(set([card.batch for card in all_cards]))
    context = {"card_list": queryset, "batches_list": batches}
    return render(request, template_name, context)
