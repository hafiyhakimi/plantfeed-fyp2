# Generated by Django 3.2.9 on 2024-06-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20240613_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodproduct',
            name='test_fix',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
