from users.views import ProjectViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')

urlpatterns = router.urls

