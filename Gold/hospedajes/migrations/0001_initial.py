# Generated by Django 5.0 on 2023-12-07 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabañas', '0001_initial'),
        ('clientes', '0002_rename_nationalidad_cliente_nacionalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('Cabaña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabañas.cabaña')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
