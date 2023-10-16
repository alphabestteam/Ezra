from django.urls import path
from .views import add_target, all_targets
from . import views

urlpatterns = [
    # Add here all the URLs you need
    path('AddTarget/', add_target),
    path('AllTargets/', all_targets),
]
