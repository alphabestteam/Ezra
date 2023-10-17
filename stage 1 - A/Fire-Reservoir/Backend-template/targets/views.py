from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from targets.models import Target
from targets.serializers import TargetSerializer
from rest_framework.decorators import api_view



@csrf_exempt
def add_target(request):
    if request.method == "POST":
        object_data = JSONParser().parse(request)
        data_deserialized = TargetSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("saved successfully!", status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("object was not well formed", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_target(request):
    update_target_data = JSONParser().parse(request)
    update_target_serializer = TargetSerializer(data=update_target_data)
    target = Target.objects.get(target_id=update_target_data["target_id"])
    update_target_serializer.update(target, update_target_data)
    return HttpResponse("updated", status=status.HTTP_200_OK)
        

def all_targets(request):
    # Implement here a get all targets function
    if request.method == "GET":
        targets = Target.objects.all()
        targets_serialized = TargetSerializer(targets, many = True)
        return JsonResponse(targets_serialized.data, safe=False)
