# Generated by Django 4.2.6 on 2023-10-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_plant', models.CharField(max_length=200)),
                ('type_plant', models.CharField(max_length=50)),
                ('price_plant', models.IntegerField()),
                ('img_plant', models.ImageField(upload_to='')),
                ('text_plant', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Plants',
        ),
    ]
