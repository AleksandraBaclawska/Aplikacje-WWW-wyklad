from django.db import models

class Gamemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    class Meta:
        db_table='games_API'
    def __str__(self):
		    return self


            

class Studiomodel(models.Model):
    studioName=models.CharField(max_length=100)
    studioOwner=models.CharField(max_length=50)
