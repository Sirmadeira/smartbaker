# Generated by Django 4.1 on 2023-10-15 18:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_alter_order_status_of_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="transaction_id",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
