# Generated by Django 4.1 on 2023-01-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_alter_order_options_order_order_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
