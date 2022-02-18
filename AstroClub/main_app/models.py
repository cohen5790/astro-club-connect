# from socket import PACKET_HOST
# from typing_extensions import Required
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from setuptools import Require

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)    
    def __str__(self):
        return f"Photo for character_id:  @{self.url}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    social_handles = models.CharField(max_length=500, default='', blank=True)

class Horoscope(models.Model):
    CAPRICORN = 'CP'
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
    ARIES = 'AR'
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
        (ARIES, 'Aries')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    horoscope = models.CharField(
        max_length=2,
        choices=HOROSCOPE_CHOICES,
        default='Capricorn',
        )
    

    