from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Card, Batch
from .forms import CardForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "cardfactory/index.html"


class CardListView(LoginRequiredMixin, ListView):
    template_name = "cardfactory/card_list.html"
    model = Card
    context_object_name = "card_list"
    ordering = ["lot", "card_number", "pk"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["batches_list"] = Batch.objects.all()
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
    batches = Batch.objects.all()
    context = {"batch_list": batches}
    return render(request, template_name, context)


@login_required
def card_list_per_batch(request, pk):
    template_name = "cardfactory/card_list.html"
    all_cards = Card.objects.all()
    batch = Batch.objects.get(pk=pk)
    queryset = all_cards.filter(lot=batch).order_by("card_number", "pk")
    batches = Batch.objects.all()
    context = {"card_list": queryset, "batches_list": batches}
    return render(request, template_name, context)


@login_required
def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    form = CardForm(request.POST or None, instance=card)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            url = reverse("cardfactory:card_detail", args=[card.pk])
            return HttpResponseRedirect(url)
    return render(
        request, "cardfactory/edit_card.html", context={"form": form, "card": card}
    )
