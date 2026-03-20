from .models import project
from rest_framework import viewsets, permissions
from .serializers import projectSerializers

class projectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = projectSerializers

