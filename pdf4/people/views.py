from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from people.models import Person,Parent
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer, ParentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        people_list = list(Person.objects.all().values())
        return JsonResponse(people_list, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse('not good', status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
            person_ser.update(person, data)
            return HttpResponse("updated!", status=status.HTTP_200_OK)
        else:
            return HttpResponse("not updated", status=status.HTTP_400_BAD_REQUEST)

'''
##################################################
part 5
##################################################
'''
@csrf_exempt
def get_all_parents(request):
    if request.method == "GET":
        parents_list = Parent.objects.all()
        parents_data = ParentSerializer(parents_list, many=True).data
        return JsonResponse(parents_data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
def add_parent(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        data_deserialized = ParentSerializer(data=data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("saved!", status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("not good", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("not POST", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def remove_parent(request, tz):
    if request.method == "DELETE":
        parent = Parent.objects.get(tz=tz)
        parent.delete()
        return HttpResponse("deleted!", status=status.HTTP_200_OK)


@csrf_exempt
def update_parent(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            parent = Parent.objects.get(tz=data["tz"])
        except ObjectDoesNotExist:
            return HttpResponse(
                "object doesn't exist", status=status.HTTP_404_NOT_FOUND
            )
        parent_ser = ParentSerializer(parent, data=data)

        if parent_ser.is_valid():
            parent_ser.update(parent, data)
            return HttpResponse("updated!", status=status.HTTP_200_OK)
        else:
            return HttpResponse("not updated", status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def associate_kid_to_parent(request, k_tz, p_tz):
    if request.method == "PUT":
        try:
            kid = Person.objects.get(tz=k_tz)
            parent = Parent.objects.get(tz=p_tz)
        except ObjectDoesNotExist:
            return HttpResponse('please enter a valid tz for kid and parent', status=status.HTTP_404_NOT_FOUND)
        parent.kids.add(kid)
        return HttpResponse("associated", status=status.HTTP_200_OK)
    else:
        return HttpResponse('not good', status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def get_info_of_parent(request, p_tz):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(tz=p_tz)
            parent_ser = ParentSerializer(parent)
        except ObjectDoesNotExist:
            return HttpResponse('please enter a valid tz for parent', status=status.HTTP_404_NOT_FOUND)

        list_of_kids = [parent_ser.data]
        
        for x in parent_ser.data["kids"]:
            kid = Person.objects.get(tz=x)
            kid_ser = PersonSerializer(kid)
            list_of_kids.append(kid_ser.data)
        return JsonResponse(list_of_kids, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse('bad request', status=status.HTTP_405_METHOD_NOT_ALLOWED)

def kid_age(kid_ser):
    date = kid_ser["date_of_birth"]
    date_obj = datetime.strptime(date, r"%Y-%m-%d")
    return 2023 - date_obj.year


@csrf_exempt
def get_rich_kids(request):
    if request.method == 'GET':
        list_rich_kids = []

        # getting all parents that earn more than 50000.00 a month.
        parents_list = list(Parent.objects.filter(salary__gte=50000.00))
        parents_data = ParentSerializer(parents_list, many=True).data
        for parent in parents_data:
            for x in parent["kids"]:
                kid = Person.objects.get(tz=x)
                kid_ser = PersonSerializer(kid)
                if kid_age(kid_ser.data) < 18:
                    list_rich_kids.append(kid_ser.data)
        return JsonResponse(list_rich_kids, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse('not good', status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def get_parents(request, kid_tz):
    if request.method == 'GET':
        list_of_parents = []

        parents = Parent.objects.all()
        parents_ser = ParentSerializer(parents, many=True).data
        for parent in parents_ser:
            print(parent)
            for kid in parent["kids"]:
                if kid == kid_tz:
                    list_of_parents.append(parent)


        return JsonResponse(list_of_parents, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse("not good",status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # the other way is to create a function in person get_parents() and there it would get the parents
    # using the instance.

@csrf_exempt
def get_kids(request, parent_tz):
    if request.method == 'GET':
        list = []
        parent = Parent.objects.get(tz=parent_tz)
        parent_ser = ParentSerializer(parent).data

        for kid in parent_ser['kids']:
            kid = Person.objects.get(tz=kid)
            kid_ser = PersonSerializer(kid).data
            list.append(kid_ser)
        
        return JsonResponse(list, status=status.HTTP_200_OK, safe=False)
    else:
        return HttpResponse('not good',status=status.HTTP_405_METHOD_NOT_ALLOWED)