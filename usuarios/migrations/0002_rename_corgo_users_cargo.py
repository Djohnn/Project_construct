# Generated by Django 5.0.6 on 2024-07-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='corgo',
            new_name='cargo',
        ),
    ]