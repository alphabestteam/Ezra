from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from people.models import Person
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@csrf_exempt
def get_all_people(request):
    people_list = list(Person.objects.all().values())
    return JsonResponse(people_list, status=status.HTTP_200_OK, safe=False)


@csrf_exempt
def add_person(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        data_deserialized = PersonSerializer(data=data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("saved!", status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("not good", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("not POST", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def remove_person(request, tz):
    if request.method == "DELETE":
        person = Person.objects.get(tz=tz)
        person.delete()
        return HttpResponse("deleted!", status=status.HTTP_200_OK)


@csrf_exempt
def update_person(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            person = Person.objects.get(tz=data["tz"])
        except ObjectDoesNotExist:
            return HttpResponse(
                "object doesn't exist", status=status.HTTP_404_NOT_FOUND
            )
        person_ser = PersonSerializer(person, data=data)

        if person_ser.is_valid():
            person_ser.save()
            return HttpResponse("updated!", status=status.HTTP_200_OK)
        else:
            return HttpResponse("not updated", status=status.HTTP_400_BAD_REQUEST)
