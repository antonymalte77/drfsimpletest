from rest_framework import serializers
from .models import project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'f_creacion')  
        read_only_fields = ('f_creacion', )