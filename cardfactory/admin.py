from django.contrib import admin

# Register your models here.
from .models import Card, Batch


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["title", "lot"]
    list_filter = ["lot"]


admin.site.register(Card, CardAdmin)
admin.site.register(Batch)
