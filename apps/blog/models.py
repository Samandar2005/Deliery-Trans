from django.db import models

# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  image = models.ImageField(upload_to='blog/')
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)


  def __str__(self):
        return self.title