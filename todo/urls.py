from rest_framework import routers
from .views import ToDoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'todo', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
