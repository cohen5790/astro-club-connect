# from socket import PACKET_HOST
# from typing_extensions import Required
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Photo for character_id:  @{self.url}"

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
    horoscope = models.CharField(
        max_length=2,
        choices=HOROSCOPE_CHOICES,
        default='CAPRICORN',
        )
    