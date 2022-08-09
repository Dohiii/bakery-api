from django.db import models
from locations.models import City, Country, Province
from django.conf import settings


# Create your models here.
class Bakery(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    # opening_hours
    specialization = models.CharField(max_length=255, null=True)
    is_pizza = models.BooleanField(default=False)
    is_cakes = models.BooleanField(default=False)
    is_open_weekends = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='bakeries')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='bakeries')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='bakeries')
    street = models.CharField('Street Name', max_length=255)
    building_number = models.IntegerField()
    flat_number = models.IntegerField()
    zip_code = models.CharField("ZIP / Postal code", max_length=12,)
    latitude = models.DecimalField(max_digits=8, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class BakeryOwner(models.Model):
    pass


# WEEKDAYS = [
#   (1, _("Monday")),
#   (2, _("Tuesday")),
#   (3, _("Wednesday")),
#   (4, _("Thursday")),
#   (5, _("Friday")),
#   (6, _("Saturday")),
#   (7, _("Sunday")),
# ]
#
# class OpeningHours(models.Model):
#
#     weekday = models.IntegerField(choices=WEEKDAYS)
#     from_hour = models.TimeField()
#     to_hour = models.TimeField()
#
#     class Meta:
#         ordering = ('weekday', 'from_hour')
#         unique_together = ('weekday', 'from_hour', 'to_hour')
#
#     def __unicode__(self):
#         return u'%s: %s - %s' % (self.get_weekday_display(),
#                                  self.from_hour, self.to_hour)
