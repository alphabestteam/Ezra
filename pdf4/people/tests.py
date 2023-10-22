from django.test import TestCase
from .models import Parent, Person


# Create your tests here.
class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Shira", tz= 4,date_of_birth= "2001-08-09",city= "Rishon LeZion")
        Person.objects.create(name="Yoav", tz=19, date_of_birth = "1989-08-21", city="Herzliya")

    def test_is_over_18(self):
        """Checks if person is over 18 years old"""
        shira = Person.objects.get(name="Shira")
        yoav = Person.objects.get(name="Yoav")
        self.assertEqual(shira.test_person_is_over_18(), True)
        self.assertEqual(yoav.test_person_is_over_18(), True)