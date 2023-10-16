from django.urls import path
from .views import add_target
from . import views

urlpatterns = [
    # Add here all the URLs you need
    path('AddTarget/', add_target)
]
