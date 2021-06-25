from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hired_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10


# to be able to add listing from admin panel
admin.site.register(Realtor, RealtorAdmin)
