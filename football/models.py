from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def hrac_path(instance, filename):
    return "hrac/" + str(instance.prijmeni) + "/fotka/" + filename


class Soutez(models.Model):
    nazev_souteze = models.CharField(max_length=80, verbose_name="Název souteže")

    pocet_tymu = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(2)],
                                     verbose_name="Počet týmů v souteži")

    class Meta:
        ordering = ['nazev_souteze']
        verbose_name_plural = "Soutěže"

    def __str__(self):
        return self.nazev_souteze


class Klub(models.Model):
    nazev_klubu = models.CharField(max_length=70, verbose_name="Název klubu")

    rok_zalozeni = models.IntegerField(validators=[MaxValueValidator(2022), MinValueValidator(1850)],
                                       verbose_name="Rok zalození klubu")

    zeme = models.CharField(max_length=40, verbose_name="Země")

    mesto = models.CharField(max_length=50, verbose_name="Město")

    stadion = models.CharField(max_length=70, verbose_name="Stadion")

    soutezNazev = models.ForeignKey(Soutez, on_delete=models.CASCADE, verbose_name="Soutež")

    class Meta:
        ordering = ['nazev_klubu']
        verbose_name_plural = "Kluby"

    def __str__(self):
        return self.nazev_klubu


class Hrac(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno hráče", blank=True)

    prijmeni = models.CharField(max_length=50, verbose_name="Příjmení hráče")

    datum_narozeni = models.DateField(verbose_name="Datum narození")

    foto = models.FileField(upload_to=hrac_path, blank=True, null=True, verbose_name="Fotka hráče")

    klubNazev = models.ForeignKey(Klub, on_delete=models.CASCADE, verbose_name="Klub")

    vyska = models.IntegerField(validators=[MaxValueValidator(300), MinValueValidator(50)], verbose_name="Výška (v cm)")


    POZICE = (
        ("útočník", "útočník"),
        ("záložník", "záložník"),
        ("obránce", "obránce"),
        ("brankář", "brankář"),
    )

    pozice = models.CharField(max_length=50, choices=POZICE)

    PREFEROVANA_NOHA = (
        ("pravá", "pravá"),
        ("levá", "levá"),
    )

    preferovana_noha = models.CharField(max_length=50, choices=PREFEROVANA_NOHA, verbose_name="Preferovaná noha")

    poradi_zlaty_mic = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(1)], verbose_name="Pořadí (zlatý míč)")

    class Meta:
        ordering = ['prijmeni']
        verbose_name_plural = "Hráči"

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"
