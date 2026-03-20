from rest_framework import serializers
from .models import Project # <--- Cambia project por Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project # <--- Cambia project por Project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'f_creacion')