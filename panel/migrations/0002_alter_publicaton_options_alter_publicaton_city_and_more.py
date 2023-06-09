# Generated by Django 4.2.1 on 2023-05-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaton',
            options={'ordering': ['city', 'time'], 'verbose_name': 'Время публикаций', 'verbose_name_plural': 'Время публикаций'},
        ),
        migrations.AlterField(
            model_name='publicaton',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='publicaton',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
