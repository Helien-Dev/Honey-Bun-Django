# Generated by Django 5.0.4 on 2024-05-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bun_Store', '0008_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_offer',
            field=models.BooleanField(default=False),
        ),
    ]