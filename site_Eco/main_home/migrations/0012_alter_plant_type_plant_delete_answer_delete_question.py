# Generated by Django 4.2.6 on 2023-10-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0011_alter_plant_type_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='type_plant',
            field=models.CharField(choices=[('Кактусы и суккуленты', 'Кактусы и суккуленты'), ('Декоративно-лиственные растения', 'Декоративно-лиственные растения'), ('Красиво-цветущие растения', 'Красиво-цветущие растения')], max_length=50, verbose_name='Вид растения'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
