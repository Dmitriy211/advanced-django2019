from django.contrib import admin
from users.models import Project, Profile, TaskComment, TaskDocument, Task

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'address', 'address2', 'registration_date', 'user')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creator')


# @admin.register(Block)
# class BlockAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'type', 'project')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator')


@admin.register(TaskDocument)
class TaskDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'creator', 'task')


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'created_at', 'task')
