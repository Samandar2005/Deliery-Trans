from django.db import models

# Create your models here.
class Client(models.Model):
  image = models.ImageField(upload_to='client/')
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)

  def __str__(self):
        return f"Image Adres: {self.image}"