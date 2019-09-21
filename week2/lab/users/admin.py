from django.contrib import admin
from users.models import ExtendedUser, Profile

@admin.register(ExtendedUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'address', 'address2', 'registration_date', 'user',)
