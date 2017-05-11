from rest_framework import serializers

from apps.core.models import Article
from apps.core.serializers.category import CategorySerializer


class ArticleSafeMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )

    categories = CategorySerializer(
        many=True,
    )

    since_created_at = serializers.ReadOnlyField()
    since_updated_at = serializers.ReadOnlyField()
    since_deleted_at = serializers.ReadOnlyField()
    display_created_at = serializers.ReadOnlyField()
    display_updated_at = serializers.ReadOnlyField()
    display_deleted_at = serializers.ReadOnlyField()


class ArticleCreateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = (
            'created_by',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )


class ArticleUpdateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = (
            'created_by',
            'is_anonymous',
            'use_signature',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )
