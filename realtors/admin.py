from django.contrib import admin

from .models import Realtor

# to be able to add listing from admin panel
admin.site.register(Realtor)
