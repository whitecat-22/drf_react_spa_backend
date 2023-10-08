from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_fields = ('name',)
