# Generated by Django 4.2.7 on 2023-12-04 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0002_rename_fecha_reserva_fecha_and_more'),
        ('servicios', '0002_servicio_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservaservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('idReserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio')),
            ],
        ),
    ]
