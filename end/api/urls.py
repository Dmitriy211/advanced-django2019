from .views import ArticleViewSet, ArticleImageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, base_name='api')
router.register('images', ArticleImageViewSet, base_name='api')

urlpatterns = router.urls