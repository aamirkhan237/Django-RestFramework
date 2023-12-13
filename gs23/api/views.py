from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(["GET","POST","PUT","DELETE","PATCH"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method=="GET":
        id=pk #direct parsed data
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Inserted Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="PUT":  #complete update
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response("Complete Data Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=="PATCH":
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partial Data Updated")
        return Response(serializer.errors)


    if request.method=="DELETE":
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response("Data Deleted")

       

