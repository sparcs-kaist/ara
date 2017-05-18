from rest_framework import serializers

from apps.core.models import DocumentUpdateLog


class DocumentUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUpdateLog
        fields = '__all__'
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )

    previous_document = serializers.JSONField()
