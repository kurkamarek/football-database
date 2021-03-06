# Generated by Django 4.0.4 on 2022-05-29 18:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import football.models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hrac',
            options={'ordering': ['prijmeni'], 'verbose_name_plural': 'Hráči'},
        ),
        migrations.AlterModelOptions(
            name='klub',
            options={'ordering': ['nazev_klubu'], 'verbose_name_plural': 'Kluby'},
        ),
        migrations.AlterModelOptions(
            name='soutez',
            options={'ordering': ['nazev_souteze'], 'verbose_name_plural': 'Soutěže'},
        ),
        migrations.AddField(
            model_name='hrac',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=football.models.hrac_path, verbose_name='Fotka hráče'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='datum_narozeni',
            field=models.DateField(verbose_name='Datum narození'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='jmeno',
            field=models.CharField(blank=True, max_length=50, verbose_name='Jméno hráče'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='pozice',
            field=models.CharField(choices=[('utocnik', 'útočník'), ('zaloznik', 'záložník'), ('obrance', 'obránce'), ('brankar', 'brankář')], max_length=50),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='preferovana_noha',
            field=models.CharField(choices=[('prava', 'pravá'), ('leva', 'levá')], max_length=50, verbose_name='Preferovaná noha'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='prijmeni',
            field=models.CharField(max_length=50, verbose_name='Příjmení hráče'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='vyska',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(50)], verbose_name='Výška (v cm)'),
        ),
        migrations.AlterField(
            model_name='klub',
            name='mesto',
            field=models.CharField(max_length=50, verbose_name='Město'),
        ),
        migrations.AlterField(
            model_name='klub',
            name='nazev_klubu',
            field=models.CharField(max_length=70, verbose_name='Název klubu'),
        ),
        migrations.AlterField(
            model_name='klub',
            name='rok_zalozeni',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1850)], verbose_name='Rok zalození klubu'),
        ),
        migrations.AlterField(
            model_name='klub',
            name='soutezNazev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.soutez', verbose_name='Soutež'),
        ),
        migrations.AlterField(
            model_name='klub',
            name='zeme',
            field=models.CharField(max_length=40, verbose_name='Země'),
        ),
        migrations.AlterField(
            model_name='soutez',
            name='nazev_souteze',
            field=models.CharField(max_length=80, verbose_name='Název souteže'),
        ),
        migrations.AlterField(
            model_name='soutez',
            name='pocet_tymu',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(2)], verbose_name='Počet týmů v souteži'),
        ),
    ]
