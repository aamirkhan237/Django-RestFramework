from django.shortcuts import render
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .models import Student


# Create your views here.
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print("Student object", stu)
    serializer = StudentSerializer(stu)  # converted into python
    # print("serializer", serializer)
    # print("serializer data", serializer.data)
    # json_data = JSONRenderer().render(serializer.data)  # converted into json
    # print(json_data)

    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(
        serializer.data, safe=True
    )  # dic obj allowed only when safe=True


def student_list(request):
    stu = Student.objects.all()
    # print("Student object", stu)
    serializer = StudentSerializer(stu, many=True)  # converted into python
    # print("serializer", serializer)
    # print("serializer data", serializer.data)
    # json_data = JSONRenderer().render(serializer.data)  # converted into json
    # print(json_data)

    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(
        serializer.data, safe=False
    )  # dic obj allowed only when safe=True
