# Generated by Django 5.0.4 on 2024-05-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bun_Store', '0006_alter_customer_email_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
