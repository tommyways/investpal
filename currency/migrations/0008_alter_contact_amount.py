# Generated by Django 4.1.7 on 2023-03-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0007_rename_withdraw_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="amount",
            field=models.IntegerField(blank=True),
        ),
    ]