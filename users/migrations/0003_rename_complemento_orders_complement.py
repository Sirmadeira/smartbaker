# Generated by Django 4.1 on 2023-01-13 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_orders_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orders",
            old_name="complemento",
            new_name="complement",
        ),
    ]
