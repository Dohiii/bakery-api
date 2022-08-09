from django.db import models
from django.conf import settings


# Create your models here.
class Country(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, unique=True)
    language = models.CharField(max_length=255)
    language_short = models.CharField(max_length=3, blank=True)
    capital = models.CharField(max_length=255, blank=True)
    dialing_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Province(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='provinces', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    is_capital = models.BooleanField(default=False)
    province = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
