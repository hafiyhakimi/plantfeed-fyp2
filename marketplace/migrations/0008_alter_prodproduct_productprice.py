# Generated by Django 3.2.9 on 2024-06-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_prodproduct_productsold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodproduct',
            name='productPrice',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]