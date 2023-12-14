from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#IsAdminUser= staff(True)
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[] 
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser,]  
    # permission_classes=[IsAuthenticatedOrReadOnly] 
    # permission_classes=[DjangoModelPermissions]  
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]  
    # permission_classes=[AllowAny,]  

