# Generated by Django 4.1 on 2022-08-27 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_favorites'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
