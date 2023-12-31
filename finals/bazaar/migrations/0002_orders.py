# Generated by Django 4.2.7 on 2023-12-11 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bazaar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bazaar.items"
                    ),
                ),
            ],
        ),
    ]
