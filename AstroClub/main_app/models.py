# from socket import PACKET_HOST
from django.db import models
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Photo for character_id:  @{self.url}"


class User(models.Model):
    name = models.CharField(max_length=100)

    # def __str__(self):
    #     return f'hello {self}'

class Profile(models.Model):
    CAPRICORN = 'CA'
    TAURUS = 'TA'
    GEMINI = 'GE'
    CANCER = 'CA'
    LEO = 'LE'
    VIRGO = 'VI'
    LIBRA = 'LI'
    SCORPIO = 'SC'
    SAGITTARIUS = 'SA'
    AQUARIUS = 'AQ'
    PISCES = 'PI'
    HOROSCOPE_CHOICES = [
        (CAPRICORN, 'Capricorn'),
        (TAURUS, 'Taurus'),
        (GEMINI, 'Gemini'),
        (CANCER, 'Cancer'),
        (LEO, 'Leo'),
        (VIRGO, 'Virgo'),
        (LIBRA, 'Libra'),
        (SCORPIO, 'Scorpio'),
        (SAGITTARIUS, 'Sagittarius'),
        (AQUARIUS, 'Aquarius'),
        (PISCES, 'Pisces'),
    ]
    user_name = models.CharField(max_length=20),
    password = models.CharField(max_length=20),
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    profile_pic = models.ForeignKey(Photo, on_delete=models.SET_NULL),
    horoscope = models.CharField(
        max_length=2,
        choices=HOROSCOPE_CHOICES,
        default='CAPRICORN',
        )
    

