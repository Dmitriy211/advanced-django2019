from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from users.serializers import *
from users.models import *


class ProjectViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
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
        instance = self.get_object()
        res = f'{instance.name}: tasks'

        return Response(res)

