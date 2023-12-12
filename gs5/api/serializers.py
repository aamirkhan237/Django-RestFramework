from rest_framework import serializers
from .models import Student


#validators
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('starts with R')
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[starts_with_r])
    city = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #field level validation
    def create(self,validated_data): 
        return Student.objects.create(**validated_data)
    
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



