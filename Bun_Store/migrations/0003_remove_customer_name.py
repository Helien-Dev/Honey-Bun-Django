# Generated by Django 5.0.4 on 2024-04-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bun_Store', '0002_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
