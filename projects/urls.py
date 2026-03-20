from rest_framework import routers
from .views import ProjectViewSet # Solo importamos desde views

router = routers.DefaultRouter()

# Asegúrate de usar ProjectViewSet (con P mayúscula)
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls