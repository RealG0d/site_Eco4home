# Generated by Django 4.2.6 on 2023-10-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0002_plant_delete_plants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='img_plant',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
