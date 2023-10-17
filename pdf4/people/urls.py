from django.urls import path
from . import views
urlpatterns = [
    path('getAllPeople/', views.get_all_people),
    path('addPerson/', views.add_person),
    path('removePerson/<int:tz>/', views.remove_person),
    path('updatePerson/', views.update_person),

    path('getAllParents/', views.get_all_parents),
    path('addParent/', views.add_parent),
    path('removeParent/<int:tz>/', views.remove_parent),
    path('updateParent/', views.update_parent),
]
