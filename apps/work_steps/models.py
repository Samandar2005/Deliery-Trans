from django.db import models

# Create your models here.

class Work_step(models.Model):
  title = models.CharField(max_length=200)
  body = models.CharField(max_length=200)
  image = models.ImageField(upload_to='work_step/')
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)