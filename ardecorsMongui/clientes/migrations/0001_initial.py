# Generated by Django 5.0.7 on 2024-09-17 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="clientes",
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
                (
                    "nombre",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El nombre solo puede contener letras y espacios.",
                                regex="^[a-zA-Z\\s]+$",
                            )
                        ],
                    ),
                ),
                ("contacto", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "telefono",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El número de teléfono debe tener el formato +57 seguido de 10 dígitos.",
                                regex="^\\+57[3][0-9]{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        validators=[django.core.validators.EmailValidator()],
                    ),
                ),
                ("direccion", models.TextField(blank=True, null=True)),
            ],
        ),
    ]