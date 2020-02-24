from django.contrib import admin
from houseowner.models import housedetail


# Register your models here.
class housedetailAdmin(admin.ModelAdmin):
    list_display = ['bedrooms', 'bathrooms', 'area', 'expected_rent', 'expected_advance']


admin.site.register(housedetail, housedetailAdmin)
