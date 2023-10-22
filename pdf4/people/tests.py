import json
from django.test import TestCase, Client
from .models import Person


# Create your tests here.
class PersonTestCase(TestCase):
    fixtures = ['people_fixture.json']

    def setUp(self):
        Person.objects.create(name="qwe", tz= 94354,date_of_birth= "2001-08-09",city= "Rishon LeZion")
        Person.objects.create(name="Yoavi", tz=139, date_of_birth = "1989-08-21", city="Herzliya")
        self.client = Client()

    def test_is_over_18(self):
        """Checks if person is over 18 years old"""
        qwe = Person.objects.get(name="qwe")
        yoavi = Person.objects.get(name="Yoavi")
        self.assertTrue(qwe.test_person_is_over_18())
        self.assertTrue(yoavi.test_person_is_over_18())

    def test_get_all_parents(self):
        """Checks to see if getAllParents return 200 and the right length"""
        response = self.client.get("/api/getAllParents/")
        self.assertEqual(response.status_code, 200)

        print("*****************")
        print(response.content)
        json_data = json.loads(response.content)
        self.assertEqual(len(json_data), 7)

    
        