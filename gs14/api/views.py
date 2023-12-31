from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
# Create your views here.

class LCStudentAPI(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)
    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)