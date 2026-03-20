from rest_framework import viewsets, permissions
from .models import Project # <--- Cambia project por Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # <--- Cambia project por Project
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
