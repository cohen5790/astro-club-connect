from django.contrib import admin


from .models import Horoscope, Photo, Profile

# Register your models here.

admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(Horoscope)
