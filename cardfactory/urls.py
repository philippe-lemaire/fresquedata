from django.urls import path


from . import views

app_name = "cardfactory"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cartes", views.CardListView.as_view(), name="card_list"),
    path(
        "cartes_vue_compacte",
        views.CardListCompactView.as_view(),
        name="card_compact_list",
    ),
    path("cartes/<int:pk>", views.CardDetailView.as_view(), name="card_detail"),
    path(
        "cartes/lot_<int:batch>", views.card_list_per_batch, name="card_list_per_batch"
    ),
    path("lots", views.batch_list, name="batch_list"),
]
