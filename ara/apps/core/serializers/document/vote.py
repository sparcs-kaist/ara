from rest_framework import serializers

from apps.core.models import DocumentVote


class DocumentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVote
        fields = '__all__'
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )


class DocumentVoteCreateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVote
        fields = (
            'is_up',
            'created_by',
            'created_on',
        )


class DocumentVoteUpdateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVote
        fields = (
            'is_up',
        )
