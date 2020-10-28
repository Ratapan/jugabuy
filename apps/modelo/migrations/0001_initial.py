# Generated by Django 3.1.1 on 2020-10-17 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cesta',
            fields=[
                ('ce_id', models.AutoField(primary_key=True, serialize=False)),
                ('ce_fe_crec', models.DateField()),
                ('ce_status', models.IntegerField(max_length=1)),
                ('ce_total', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciu', models.AutoField(primary_key=True, serialize=False)),
                ('desc_ciu', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('j_id', models.AutoField(primary_key=True, serialize=False)),
                ('j_nom', models.CharField(max_length=100)),
                ('j_plt', models.CharField(max_length=10)),
                ('j_desc', models.CharField(max_length=2000)),
                ('j_port', models.ImageField(upload_to='')),
                ('j_price', models.IntegerField()),
                ('j_fe_sal', models.DateField()),
                ('j_status', models.IntegerField()),
                ('j_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_reg', models.AutoField(primary_key=True, serialize=False)),
                ('desc_reg', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('desc_rol', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('us_id', models.AutoField(primary_key=True, serialize=False)),
                ('us_rut', models.IntegerField(max_length=20)),
                ('us_mail', models.EmailField(max_length=254)),
                ('us_nom', models.CharField(max_length=20)),
                ('us_apes', models.CharField(max_length=40)),
                ('us_contr', models.CharField(max_length=20)),
                ('us_nac', models.DateField()),
                ('us_creac', models.DateField()),
                ('us_tel', models.IntegerField()),
                ('us_dir', models.CharField(max_length=50)),
                ('us_sald', models.IntegerField()),
                ('id_ciud', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.ciudad')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('tr_id', models.AutoField(primary_key=True, serialize=False)),
                ('tr_mon', models.IntegerField(max_length=6)),
                ('tr_fe', models.DateField()),
                ('tr_met_pago', models.IntegerField(max_length=16)),
                ('tr_tipo', models.CharField(max_length=20)),
                ('us_rut', models.IntegerField(max_length=20)),
                ('comp_id', models.IntegerField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('key_id', models.AutoField(primary_key=True, serialize=False)),
                ('key_desc', models.IntegerField(max_length=20)),
                ('compra_id', models.IntegerField(max_length=20)),
                ('j_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.juego')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('detcom_id', models.AutoField(primary_key=True, serialize=False)),
                ('detcom_can', models.IntegerField(max_length=2)),
                ('detcom_price', models.IntegerField(max_length=7)),
                ('compr_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.cesta')),
                ('juego_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.juego')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('det_id', models.AutoField(primary_key=True, serialize=False)),
                ('det_can', models.IntegerField(max_length=2)),
                ('det_price', models.IntegerField(max_length=7)),
                ('det_status', models.IntegerField(max_length=2)),
                ('cesta_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.cesta')),
                ('jueg_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.juego')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_cod', models.IntegerField()),
                ('com_fe', models.DateField()),
                ('com_total', models.IntegerField(max_length=20)),
                ('us_rut', models.IntegerField(max_length=20)),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.region'),
        ),
        migrations.AddField(
            model_name='cesta',
            name='us_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.usuario'),
        ),
        migrations.CreateModel(
            name='biblioteca',
            fields=[
                ('bibl_id', models.AutoField(primary_key=True, serialize=False)),
                ('juego_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.juego')),
                ('usu_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.usuario')),
            ],
        ),
    ]