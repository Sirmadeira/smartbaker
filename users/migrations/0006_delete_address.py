# Generated by Django 4.1 on 2023-01-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_address_delete_orders"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Address",
        ),
    ]
