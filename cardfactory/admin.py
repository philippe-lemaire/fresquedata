from django.contrib import admin

# Register your models here.
from .models import Card


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["title", "batch"]
    list_filter = ["batch"]


admin.site.register(Card, CardAdmin)
