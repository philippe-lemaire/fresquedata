from django.contrib import admin

# Register your models here.
from .models import Card, Batch


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["title", "batch", "batch_foreign"]
    list_filter = ["batch"]


admin.site.register(Card, CardAdmin)
admin.site.register(Batch)
