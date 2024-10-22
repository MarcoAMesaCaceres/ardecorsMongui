# Generated by Django 5.0.7 on 2024-08-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArticuloAyuda",
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
                ("titulo", models.CharField(max_length=255)),
                ("contenido", models.TextField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("ultima_actualizacion", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]