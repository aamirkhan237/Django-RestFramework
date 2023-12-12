from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
# Create your views here.


class StudentAPI(APIView):
    def get(self,request,format=None,pk=None):
        id=pk #direct parsed data
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Inserted Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response("Complete Data Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partial Data Updated")
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response("Data Deleted")

       


