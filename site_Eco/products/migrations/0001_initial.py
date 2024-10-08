# Generated by Django 4.2.6 on 2023-11-13 18:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category_plant', models.CharField(max_length=200, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_plant', models.CharField(max_length=200, verbose_name='Название растения')),
                ('price_plant', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена')),
                ('img_plant', models.ImageField(blank=True, upload_to='media', verbose_name='Картинка товара')),
                ('text_plant', models.TextField(verbose_name='Описание товара')),
                ('sale_plant', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Процент скидки')),
                ('type_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Categorys', to='products.categoryplant', verbose_name='Категория')),
            ],
        ),
    ]
