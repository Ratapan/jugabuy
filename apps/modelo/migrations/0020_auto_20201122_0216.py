# Generated by Django 3.1.2 on 2020-11-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0019_auto_20201109_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='j_fe_sal',
            field=models.CharField(max_length=15, verbose_name='Fecha de salida'),
        ),
    ]
