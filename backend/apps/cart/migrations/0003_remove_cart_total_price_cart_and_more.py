# Generated by Django 5.0.4 on 2024-06-10 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price_cart',
        ),
        migrations.RemoveField(
            model_name='cart_detail',
            name='total',
        ),
    ]