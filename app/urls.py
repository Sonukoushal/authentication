from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', obtain_auth_token),  # Token generate karne ka URL
]

