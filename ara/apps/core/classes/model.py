import datetime

from django.db import models


class MetaInfoManager(models.Manager):
    def get_queryset(self):
        queryset = super(MetaInfoManager, self).get_queryset()

        queryset = queryset.filter(deleted_at=None)

        return queryset


class MetaInfoModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성 시간',
    )
    updated_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='수정 시간',
    )
    deleted_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='삭제 시간',
    )

    objects = MetaInfoManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.datetime.now()
        self.save()

        return self
