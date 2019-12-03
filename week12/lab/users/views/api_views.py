from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from users.models import ExtendedUser, Profile
from users.serializers import ExtendedUserSerializer, ProfileSerializer

import logging

logger = logging.getLogger(__name__)


class RegisterAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = ExtendedUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"User '{serializer.data.get('username')}' singed up")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPIView(APIView):
    http_method_names = ['get', 'put']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer = ProfileSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
