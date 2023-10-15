from django.urls import path
from .views import get_random_number, get_user_random, get_current_time, get_length_of_word

urlpatterns = [
    path('getRandomNumber/', get_random_number),
    path('getRandomNumber/<int:number>/', get_user_random),

    path('getServerTime/', get_current_time),
    path('getLengthOfWord/<str:word>/', get_length_of_word),


]