from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']


#class Level Validation


#validators
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('starts with R')
    


    



