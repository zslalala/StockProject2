from django.db import models

# Create your models here.
class StockInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=32)
    market_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'StockInfo'