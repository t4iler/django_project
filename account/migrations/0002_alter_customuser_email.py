# Generated by Django 4.1 on 2022-08-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', editable=False, max_length=254, unique=True, verbose_name='email adress'),
        ),
    ]
