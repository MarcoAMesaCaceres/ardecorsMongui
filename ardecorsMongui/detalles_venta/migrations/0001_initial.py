# Generated by Django 5.0.7 on 2024-08-02 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DetalleVenta",
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
                ("cantidad", models.IntegerField()),
                (
                    "precio_unitario",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
            ],
        ),
    ]
