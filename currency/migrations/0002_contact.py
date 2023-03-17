# Generated by Django 4.1.7 on 2023-03-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("receiver_wallet", models.TextField(blank=True)),
                ("cryptocurrency", models.TextField(blank=True)),
                ("amount", models.TextField(blank=True)),
            ],
        ),
    ]