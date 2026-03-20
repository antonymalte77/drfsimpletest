from rest_framework import serializers
from .models import project # Asegúrate de que en models.py la clase sea 'project'

class ProjectSerializer(serializers.ModelSerializer): # <--- DEBE LLAMARSE ASÍ
    class Meta:
        model = project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'f_creacion')   
        read_only_fields = ('f_creacion', )