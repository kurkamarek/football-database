from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Soutez(models.Model):
    nazev_souteze = models.CharField(max_length=80, verbose_name="Název souteže")

    pocet_tymu = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(2)], verbose_name="Počet týmů v souteži")

    class Meta:
        ordering = ['nazev_souteze']

    def __str__(self):
        return self.nazev_souteze

class Klub(models.Model):
    nazev_klubu = models.CharField(max_length=70, verbose_name="Název klubu")

    rok_zalozeni = models.IntegerField(validators=[MaxValueValidator(2022),MinValueValidator(1850)], verbose_name="Rok zalození klubu")

    zeme = models.CharField(max_length=40, verbose_name="Země")

    mesto = models.CharField(max_length=50, verbose_name="Město")

    stadion = models.CharField(max_length=70, verbose_name="Stadion")

    soutezNazev = models.ForeignKey(Soutez, on_delete=models.CASCADE, verbose_name="Soutež")

    class Meta:
        ordering = ['nazev_klubu']

    def __str__(self):
        return self.nazev_klubu

class Hrac(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno hráče")

    prijmeni = models.CharField(max_length=50, verbose_name="Příjmení hrace")

    datum_narozeni = models.DateField(verbose_name="Datum narození")

    klubNazev = models.ForeignKey(Klub, on_delete=models.CASCADE, verbose_name="Klub")

    vyska = models.IntegerField(validators=[MaxValueValidator(300),MinValueValidator(50)], verbose_name="Výška (v cm)")

    POZICE = (
        ("utocnik", "útočník"),
        ("zaloznik", "záložník"),
        ("obrance", "obránce"),
        ("brankar", "brankář"),
    )

    pozice = models.CharField(max_length=50, choices=POZICE)

    PREFEROVANA_NOHA = (
        ("prava", "pravá"),
        ("leva", "levá"),
    )

    preferovana_noha = models.CharField(max_length=50, choices=PREFEROVANA_NOHA, verbose_name="Preferovaná noha")

    class Meta:
        ordering = ['prijmeni']

    def __str__(self):
        return self.prijmeni








