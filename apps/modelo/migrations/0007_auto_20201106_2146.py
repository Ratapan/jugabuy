# Generated by Django 3.1.2 on 2020-11-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0006_auto_20201105_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nom_user',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='username'),
        ),
    ]
