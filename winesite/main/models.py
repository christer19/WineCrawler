from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=200)
    winery = models.CharField(max_length=200)
    crawl_date = models.DateTimeField('Date of price')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + self.crawl_date
