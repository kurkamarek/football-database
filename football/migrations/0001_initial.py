# Generated by Django 4.0.4 on 2022-04-22 17:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soutez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_souteze', models.CharField(max_length=80, verbose_name='Nazev souteze')),
                ('pocet_tymu', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(2)], verbose_name='Pocet tymu v soutezi')),
            ],
            options={
                'ordering': ['nazev_souteze'],
            },
        ),
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_klubu', models.CharField(max_length=70, verbose_name='Nazev klubu')),
                ('rok_zalozeni', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1850)], verbose_name='Datum zalozeni klubu')),
                ('zeme', models.CharField(max_length=40, verbose_name='Zeme')),
                ('mesto', models.CharField(max_length=50, verbose_name='Mesto')),
                ('stadion', models.CharField(max_length=70, verbose_name='Stadion')),
                ('soutezNazev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.soutez', verbose_name='Soutez')),
            ],
            options={
                'ordering': ['nazev_klubu'],
            },
        ),
        migrations.CreateModel(
            name='Hrac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=50, verbose_name='Jmeno hrace')),
                ('prijmeni', models.CharField(max_length=50, verbose_name='Prijmeni hrace')),
                ('datum_narozeni', models.DateField(verbose_name='Datum narozeni')),
                ('vyska', models.IntegerField(validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(50)], verbose_name='Vyska (v cm)')),
                ('pozice', models.CharField(choices=[('utocnik', 'Utocnik'), ('zaloznik', 'Zaloznik'), ('obrance', 'Obrance'), ('brankar', 'Brankar')], max_length=50)),
                ('preferovana_noha', models.CharField(choices=[('prava', 'Prava'), ('leva', 'Leva')], max_length=50, verbose_name='Preferovana noha')),
                ('klubNazev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.klub', verbose_name='Klub')),
            ],
            options={
                'ordering': ['jmeno'],
            },
        ),
    ]
