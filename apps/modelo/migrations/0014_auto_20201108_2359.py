# Generated by Django 3.1.2 on 2020-11-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0013_auto_20201108_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='com_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]