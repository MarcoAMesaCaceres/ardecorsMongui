# Generated by Django 4.2.9 on 2024-08-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_customuser_delete_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]