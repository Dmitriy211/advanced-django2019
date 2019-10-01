from users.views import ProjectViewSet, TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')
router.register('tasks', TaskViewSet, base_name='api')

urlpatterns = router.urls
