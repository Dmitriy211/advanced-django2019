from api.views import ProductViewSet, ServiceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, base_name='api')
router.register('services', ServiceViewSet, base_name='api')

urlpatterns = router.urls
