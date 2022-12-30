from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Application(models.Model):
  where = models.CharField(max_length=200)
  where_to = models.CharField(max_length=200)
  phoone_number = PhoneNumberField(null=False, blank=False, unique=True)
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)

  def __str__(self):
        return self.where