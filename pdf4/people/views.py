from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from people.models import Person
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt


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
            return HttpResponse('saved!', status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('not good', status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse('not POST', status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt    
def remove_person(request, tz):
    if request.method == 'DELETE':
        person = Person.objects.get(tz=tz)
        person.delete()
        return HttpResponse('deleted!', status=status.HTTP_200_OK)

@csrf_exempt
def update_person(request):
    if request.method == 'PUT':
        update_p = JSONParser().parse(request)
        update_p_serialized = PersonSerializer(data=update_p)
        if update_p_serialized.is_valid():
            updated = Person.objects.get(tz= update_p_serialized["tz"])
            update_p_serialized.update(updated, update_p)
            return HttpResponse('updated!', status=status.HTTP_200_OK)
        else:
            return HttpResponse('not updated', status=status.HTTP_400_BAD_REQUEST)