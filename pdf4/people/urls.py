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
    path('associateKid<int:k_tz>2Parent<int:p_tz>/', views.associate_kid_to_parent),
    path('getInfoOfParent<int:p_tz>/', views.get_info_of_parent),
]
