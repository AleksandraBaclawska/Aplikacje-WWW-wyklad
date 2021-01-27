from django.db import models

class GameType(models.Model):
    type = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('type',)

    def __str__(self):
        return self.name

class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    WYBOR_PLCI = ((MALE, 'Male'), (FEMALE,'Female'),)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    plec = models.CharField(max_length=2, choices=WYBOR_PLCI, default=MALE)
    addres = models.CharField(max_length=300)

    class Meta:
        db_table='players_API'
        ordering = ('nazwisko',)

    def __str__(self):
        return self.imie+' '+self.nazwisko

class Gamemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    class Meta:
        db_table='games_API'
        ordering = ('name',)
    def __str__(self):
		    return str(self.name) if self.name else ''

