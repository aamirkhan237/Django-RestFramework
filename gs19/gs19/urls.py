from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
#creating Router Object

router.register('studentapi',views.StudentReadOnlyModelViewSet,basename='student')
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
