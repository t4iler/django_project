# Generated by Django 4.1 on 2022-08-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('slug',),
            },
        ),
    ]
