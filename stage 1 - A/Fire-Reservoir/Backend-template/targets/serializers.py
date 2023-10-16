from rest_framework import serializers
from .models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        # define here your model and the fields to serialize
        model = Target
        fields = "__all__"

    # not necessary. 
    # def create(self, validated_data):
    #     return super(TargetSerializer, self).create(validated_data)
    

    def update(self, instance, validated_data):
        # Implement here an update function
        return instance
