from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..serializers import TaskSerializer, ProjectSerializer, TaskShortSerializer, TaskFullSerializer
from ..models import Project, Task


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    @action(methods=['GET'], detail=False)
    def my(self, request):
        projects = Project.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        tasks = Project.objects.get(id=pk).task_set.all()
        serializer = TaskShortSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def task_count(self, request, pk):
        res = Project.objects.get(id=pk).tasks_count
        return Response(res)


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    serializer_class = TaskFullSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

