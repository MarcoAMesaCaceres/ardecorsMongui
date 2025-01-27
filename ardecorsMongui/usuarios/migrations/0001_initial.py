# Generated by Django 5.0.7 on 2024-08-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre", models.CharField(max_length=255)),
                ("usuario", models.CharField(max_length=255, unique=True)),
                ("contrasena", models.CharField(max_length=255)),
                (
                    "rol",
                    models.CharField(
                        choices=[
                            ("Admin", "Admin"),
                            ("Vendedor", "Vendedor"),
                            ("Comprador", "Comprador"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
