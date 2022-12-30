from django.db import models

# Create your models here.
class Shipping_cost(models.Model):
  country = models.CharField(max_length=200)
  price1 = models.IntegerField()
  price2 = models.IntegerField()

  def __str__(self):
        return self.country