from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

# Esta clase se encarga de TODA la lógica: listar, crear, ver uno solo, actualizar y borrar.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # Permitimos que cualquier persona (por ahora) pueda entrar a la API
    permission_classes = [permissions.AllowAny]
    # Le decimos qué traductor (serializer) debe usar
    serializer_class = ProjectSerializer
