# Generated by Django 5.0.6 on 2024-07-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
