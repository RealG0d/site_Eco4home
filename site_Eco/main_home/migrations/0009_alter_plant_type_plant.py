# Generated by Django 4.2.6 on 2023-10-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0008_alter_plant_type_plant_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='type_plant',
            field=models.CharField(choices=[('Декоративно-лиственные растения', 'Декоративно-лиственные растения'), ('Красиво-цветущие растения', 'Красиво-цветущие растения'), ('Кактусы и суккуленты', 'Кактусы и суккуленты')], max_length=50, verbose_name='Вид растения'),
        ),
    ]
