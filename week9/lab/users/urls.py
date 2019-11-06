from .views import ProjectViewSet, TaskViewSet, TaskDocumentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')
router.register('tasks', TaskViewSet, base_name='api')
router.register('task-documents', TaskDocumentViewSet, base_name='api')

urlpatterns = router.urls
