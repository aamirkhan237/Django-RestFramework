from rest_framework import serializers
from api.models import Company, Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id=serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'



