from django.contrib import admin

# Register your models here.
from .models import Card, Batch


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["card_number", "title", "lot"]
    list_filter = ["lot"]
    ordering = ["lot", "card_number"]


admin.site.register(Card, CardAdmin)
admin.site.register(Batch)
