from django.utils import timesince

from rest_framework import serializers

from apps.core.models import Comment
#from apps.core.serializers.category import CategorySerializer


class CommentSafeMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )

    #categories = CategorySerializer(
    #    many=True,
    #)

    since_created_at = serializers.SerializerMethodField()
    since_updated_at = serializers.SerializerMethodField()
    since_deleted_at = serializers.SerializerMethodField()

    def get_since_created_at(self, object):
        return timesince.timesince(object.created_at).split(",")[0] + ' 전'

    def get_since_updated_at(self, object):
        return timesince.timesince(object.created_at).split(",")[0] + ' 전'

    def get_since_deleted_at(self, object):
        return timesince.timesince(object.created_at).split(",")[0] + ' 전'


class CommentCreateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = (
            'created_by',
            'created_on',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )


class CommentUpdateMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = (
            'created_by',
            'is_anonymous',
            'use_signature',
            'created_on',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'deleted_at',
        )


