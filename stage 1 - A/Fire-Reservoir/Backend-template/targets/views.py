from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from targets.models import Target
from targets.serializers import TargetSerializer


@csrf_exempt
def add_target(request):
    # Implement here an add function
    # do parser.
    # call serializer
    # save
    # response to front
    if request.method == "POST":
        object_data = JSONParser().parse(request)
        data_deserialized = TargetSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return JsonResponse(
                "saved successfully!", safe=False
            )  # safe=False - telling Django to treat the return value not as a dictionary.
        else:
            return JsonResponse("object was not well formed", safe=False)


@csrf_exempt
def update_target(request):
    # Implement here an update function
    pass


def all_targets(request):
    # Implement here a get all targets function
    if request.method == "GET":
        targets = Target.objects.all()
        targets_serialized = TargetSerializer(targets, many = True)
        return JsonResponse(targets_serialized.data, safe=False)
