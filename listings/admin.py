from django.contrib import admin

from .models import Listing

# to be able to add listing from admin panel
admin.site.register(Listing)
