# Generated by Django 3.1.1 on 2020-10-21 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laramusicAPI', '0003_auto_20201019_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_year',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
