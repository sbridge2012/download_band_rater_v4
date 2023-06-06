from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Bands, Rating

# Register your models here.

admin.site.register(Bands)
admin.site.register(Rating)

