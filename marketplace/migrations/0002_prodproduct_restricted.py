# Generated by Django 3.2.9 on 2024-06-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodproduct',
            name='restricted',
            field=models.BooleanField(default=False),
        ),
    ]
