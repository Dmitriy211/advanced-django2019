from rest_framework import serializers
from .models import ExtendedUser, Profile, Project, Task, TaskDocument, TaskComment
import re


class ExtendedUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ExtendedUser
        fields = ('id', 'username', 'password', 'email', 'phone')

    def create(self, validated_data):
        user = ExtendedUser.objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        profile = Profile.objects.create(
            user=user
        )
        profile.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.SerializerMethodField()

    # user = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = ('id', 'origin', 'bio', 'address', 'web_site', 'avatar')

    def create(self, validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile

    def get_user_name(self, obj):
        if obj.user is not None:
            return obj.user.username
        return ''


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False)
    creator_name = serializers.SerializerMethodField()
    creator = ExtendedUserSerializer(read_only=True)

    class Meta:
        model = Project
        # fields = ('id', 'name', 'creator_id', 'description', 'creator')
        fields = '__all__'

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''

    def validate_name(self, value):
        spec = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if spec.search(value) is not None:
            raise serializers.ValidationError('name should not contain special characters')
        else:
            return value


# class BlockSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Block
#         fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creator_name = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status')


class TaskFullSerializer(TaskShortSerializer):
    creator_name = serializers.PrimaryKeyRelatedField(read_only=True)
    creator = serializers.HiddenField(required=False, default=serializers.CurrentUserDefault())

    def validate_name(self, value):
        spec = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if spec.search(value) is not None:
            raise serializers.ValidationError('name should not contain special characters')
        else:
            return value

    class Meta(TaskShortSerializer.Meta):
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TaskDocument
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = TaskComment
        fields = '__all__'

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''
