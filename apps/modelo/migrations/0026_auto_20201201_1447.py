# Generated by Django 3.1.2 on 2020-12-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0025_auto_20201201_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='us_nac',
            field=models.DateField(verbose_name='Nacimiento'),
        ),
    ]
