from django.contrib import admin

from apps.core.classes.admin import MetaInfoModelAdmin
from apps.session.models import *


@admin.register(UserProfile)
class UserProfileAdmin(MetaInfoModelAdmin):
    list_display = (
        'nick',
        'user',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'nick',
        'user__username',
    )
