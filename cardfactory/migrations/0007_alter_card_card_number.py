# Generated by Django 4.2.4 on 2023-11-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardfactory", "0006_card_card_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="card_number",
            field=models.IntegerField(
                blank=True, default=1, verbose_name="Numéro de carte dans le lot"
            ),
        ),
    ]
