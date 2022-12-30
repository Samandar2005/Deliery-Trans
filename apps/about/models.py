from django.db import models

# Create your models here.

class AboutCompaniy(models.Model):
  employees = models.IntegerField()
  cars = models.IntegerField()
  filials = models.IntegerField()
  transtort_companiy = models.IntegerField()
  clients = models.IntegerField()
  year = models.IntegerField()
  create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
  is_active = models.BooleanField(default=True)

  def __str__(self):
        return f"Employees: {self.employees}"