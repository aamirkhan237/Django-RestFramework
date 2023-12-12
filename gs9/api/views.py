from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view() # by default get is present @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

@api_view(['POST','GET']) 
def hello_world(request):
    if request.method=="GET":
        return Response({'msg':'This is Get Request'})
    if request.method=="POST":
        print(request.data)
        return Response({'msg':'This is post method','data':request.data})

