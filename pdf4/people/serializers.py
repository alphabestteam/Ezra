from rest_framework import serializers
from .models import Person, Parent
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ParentSerializer(PersonSerializer):
    class Meta:
        model = Parent
        fields = '__all__'