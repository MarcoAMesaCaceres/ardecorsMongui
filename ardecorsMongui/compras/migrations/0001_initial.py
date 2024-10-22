# Generated by Django 5.0.7 on 2024-08-02 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("proveedores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrdenCompra",
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
                ("fecha", models.DateField()),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proveedores.proveedor",
                    ),
                ),
            ],
        ),
    ]
