from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Transport(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='transport/')
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)

  def __str__(self):
        return self.title

class Transport_order(models.Model):
  name = models.CharField(max_length=200)
  where = models.CharField(max_length=200)
  where_to = models.CharField(max_length=200)
  phoone_number = PhoneNumberField(null=False, blank=False, unique=True)
  gmail = models.EmailField(max_length=250)
  comment_order = models.CharField(max_length=200)
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)

  def __str__(self):
        return self.name