from django.urls import path


from . import views

app_name = "cardfactory"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cartes", views.CardListView.as_view(), name="card_list"),
]
