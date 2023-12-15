from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

#IsAdminUser= staff(True)
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[C]
    # permission_classes=[IsAuthenticated]

