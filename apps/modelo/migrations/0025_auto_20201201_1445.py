# Generated by Django 3.1.2 on 2020-12-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0024_auto_20201201_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='us_nac',
            field=models.DateTimeField(verbose_name='Nacimiento'),
        ),
    ]