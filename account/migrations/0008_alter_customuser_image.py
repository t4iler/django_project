# Generated by Django 4.1 on 2022-08-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
