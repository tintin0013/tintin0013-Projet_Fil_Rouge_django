from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        ROCK = 'RK'
        POP = 'PP'
        JAZZ = 'JZ'
        CLASSICAL = 'CL'
        HIP_HOP = 'HH'
        INSTRUMENTAL = 'IN'
        REGGAE = 'RE'
        

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    like_new = models.fields.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):

    class Type(models.TextChoices):
        DISQUE = 'CD'
        VETEMENT = 'VE'
        POSTERS = 'P'
        DIVERS = 'DI'
        
    
    title = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
