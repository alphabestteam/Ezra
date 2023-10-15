from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
from datetime import datetime


# Create your views here.
def get_random_number(request):
    # generates a number between 0-1
    random_number = random.random()

    # creating http response
    response = HttpResponse(
        content=str(random_number), status=200, content_type="text/plain"
    )

    return response


def get_user_random(request, number):
    if not isinstance(number, int):
        raise Http404("please enter in an int", status=404)

    random_number = random.uniform(0, number)
    response = HttpResponse(
        content=str(random_number), status=200, content_type="text/plain"
    )

    return response


def get_current_time(request):
    current_time = datetime.now()
    response = HttpResponse(
        content=current_time.strftime("%Y-%m-%d %H:%M:%S"),
        status=200,
        content_type="text/plain",
    )

    return response


def get_length_of_word(request, word):
    length_of_word = len(word)
    response = HttpResponse(
        content=str(length_of_word), status=200, content_type="text/plain"
    )

    return response
