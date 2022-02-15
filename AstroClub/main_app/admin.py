from django.contrib import admin


from .models import User, Photo, Profile

# Register your models here.

admin.site.register(User)
admin.site.register(Photo)
admin.site.register(Profile)
