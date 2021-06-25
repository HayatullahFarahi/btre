from django.contrib import admin

from .models import Listing

# showing more than main field in admin dashboard


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # make title clickable
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'state', 'bedrooms', 'is_published',)
    # make editable published field
    list_editable = ('is_published',)


    # to be able to add listing from admin panel
admin.site.register(Listing, ListingAdmin)
