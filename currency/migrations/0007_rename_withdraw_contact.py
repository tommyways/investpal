# Generated by Django 4.1.7 on 2023-03-15 15:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0006_rename_contact_withdraw"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Withdraw",
            new_name="Contact",
        ),
    ]