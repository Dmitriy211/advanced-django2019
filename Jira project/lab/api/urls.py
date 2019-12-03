from .views import ProjectViewSet, TaskViewSet, TaskDocumentViewSet, ProjectMemberApiView
from rest_framework import routers
from django.urls import path

urlpatterns = [
    path('project-members/', ProjectMemberApiView.as_view()),
]

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')
router.register('tasks', TaskViewSet, base_name='api')
router.register('task-documents', TaskDocumentViewSet, base_name='api')

urlpatterns += router.urls
