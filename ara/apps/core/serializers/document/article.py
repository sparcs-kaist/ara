from rest_framework import serializers

from apps.core.models import Article


class ArticleSerializer(serializers.ModelSerializer):
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
