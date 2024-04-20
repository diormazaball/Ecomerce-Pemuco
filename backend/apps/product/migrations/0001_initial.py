# Generated by Django 5.0.4 on 2024-04-20 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoría de Producto',
                'verbose_name_plural': 'Categorías de Productos',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('state', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('opinion_id', models.AutoField(primary_key=True, serialize=False)),
                ('evaluation', models.IntegerField()),
                ('commentary', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
