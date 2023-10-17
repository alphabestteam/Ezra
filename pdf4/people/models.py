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
