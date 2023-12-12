from rest_framework import serializers
from .models import Student


#validators

    
    

class StudentSerializer(serializers.ModelSerializer):

    def starts_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('starts with R')
        
    name=serializers.CharField(validators=[starts_with_r])
    class Meta:
        model=Student
        fields=['id','name','roll','city']

    # Field level validators
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError("seat full,Roll must be less than 200")
        return value
    
#object Level Validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='rohit' and ct.lower()!='ranchi':
            raise serializers.ValidationError('City Must Be Ranchi')
        return data



