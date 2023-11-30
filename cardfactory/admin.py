from django.contrib import admin

# Register your models here.
from .models import Card, Batch


class CardAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["title", "lot"]
    list_filter = ["lot"]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lot":
            kwargs["queryset"] = Batch.objects.order_by("number")
        return super(CardAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


admin.site.register(Card, CardAdmin)
admin.site.register(Batch)
