from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from ..serializers import ProjectSerializer, TaskShortSerializer, TaskFullSerializer, TaskDocumentSerializer, ExtendedUserSerializer
from ..models import Project, Task, TaskDocument, ExtendedUser
import logging

logger = logging.getLogger(__name__)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created project {serializer.data.get('id')}: {serializer.data.get('name')}")

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

    @action(methods=['GET'], detail=True)
    def members(self, request, pk):
        users = ExtendedUser.objects.filter(memberships__project=pk)
        serializer = ExtendedUserSerializer(users, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin):
    serializer_class = TaskFullSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"'{self.request.user}' created task '{serializer.data.get('id')}: {serializer.data.get('name')}' "
                    f"for project '{serializer.data.get('project')}'")

    @action(methods=['GET'], detail=True)
    def documents(self, request, pk):
        documents = Task.objects.get(id=pk).taskdocument_set.all()
        serializer = TaskDocumentSerializer(documents, many=True)
        return Response(serializer.data)


class TaskDocumentViewSet(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin):
    serializer_class = TaskDocumentSerializer
    queryset = TaskDocument.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(
            f"'{self.request.user}' added document '{serializer.data.get('id')}: {serializer.data.get('file_name')}' "
            f"for task '{serializer.data.get('task')}'")
