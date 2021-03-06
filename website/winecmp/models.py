from django.db import models
from django.utils import timezone


class Wine(models.Model):
    name = models.CharField(max_length=200)
    winery = models.CharField(max_length=200)
    crawl_date = models.DateTimeField('Date of price', default=timezone.now())
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + self.crawl_date.__str__()
