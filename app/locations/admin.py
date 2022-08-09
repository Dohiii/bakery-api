from django.contrib import admin
import locations.models as models

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.Province)
admin.site.register(models.City)