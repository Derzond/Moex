from django.db import models


class Gold(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['timestamp', ]),
        ]

    last = models.FloatField(null=True)
    bid = models.FloatField(null=True)
    ask = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    open = models.FloatField(null=True)
    previousClose = models.FloatField(null=True)
    timestamp = models.DateTimeField(null=True)

    price_g = models.FloatField(null=True)
    price_kg = models.FloatField(null=True)
    previousClose_g = models.FloatField(null=True)
    previousClose_kg = models.FloatField(null=True)


class Silver(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['timestamp', ]),
        ]

    last = models.FloatField(null=True)
    bid = models.FloatField(null=True)
    ask = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    open = models.FloatField(null=True)
    previousClose = models.FloatField(null=True)
    timestamp = models.DateTimeField(null=True)

    price_g = models.FloatField(null=True)
    price_kg = models.FloatField(null=True)
    previousClose_g = models.FloatField(null=True)
    previousClose_kg = models.FloatField(null=True)


