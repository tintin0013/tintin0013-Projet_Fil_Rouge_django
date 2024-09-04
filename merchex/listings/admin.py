from django.contrib import admin
from listings.models import Band, Listing

# Register your models here.
# listings/admin.py

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'sold', 'year','band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)