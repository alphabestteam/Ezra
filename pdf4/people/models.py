from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    tz = models.IntegerField(
        primary_key=True, validators=[MaxValueValidator(limit_value=999999999)]
    )
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)

class Parent(Person):
    work_place = models.CharField(max_length=50, null=True)
    salary = models.DecimalField(decimal_places=2 , max_digits= 8, null=True)
    kids = models.ManyToManyField(Person, related_name='parents', default=[])
    