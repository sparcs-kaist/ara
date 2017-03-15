from django.contrib import admin

from apps.core.classes.admin import MetaInfoModelAdmin
from apps.core.models import *


@admin.register(Category)
class CategoryAdmin(MetaInfoModelAdmin):
    list_display = (
        'slug',
        'ko_name',
        'en_name',
    )
    search_fields = (
        'slug',
        'ko_name',
        'en_name',
    )


@admin.register(Article)
class ArticleAdmin(MetaInfoModelAdmin):
    list_filter = (
        'categories__slug',
    )
    list_display = (
        'summary',
        'created_by',
        'created_at',
        'updated_at',
        'is_anonymous',
        'is_content_erotic',
        'is_content_social',
        'use_signature',
    )
    search_fields = (
        'title',
        'content',
        'created_by',
    )


@admin.register(Comment)
class CommentAdmin(MetaInfoModelAdmin):
    list_display = (
        'summary',
        'created_by',
        'created_at',
        'updated_at',
        'is_anonymous',
        'is_content_erotic',
        'is_content_social',
        'use_signature',
    )
    search_fields = (
        'content',
        'created_by',
    )
