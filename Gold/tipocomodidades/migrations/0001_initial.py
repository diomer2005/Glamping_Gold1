# Generated by Django 4.2.7 on 2023-12-04 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabañas', '0001_initial'),
        ('comodidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipocomodidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('idCabaña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabañas.cabaña')),
                ('idComodidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comodidades.comodidad')),
            ],
        ),
    ]
