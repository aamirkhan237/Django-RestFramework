from django.shortcuts import render
import io
from .serializers import StudentSerializer

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def stucreate(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)  # complexdata
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data Created "}
            json_data = JSONRenderer().render(res)  # Use 'res' instead of 'msg'
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
