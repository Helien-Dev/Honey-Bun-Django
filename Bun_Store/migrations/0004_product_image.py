# Generated by Django 5.0.4 on 2024-04-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bun_Store', '0003_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
