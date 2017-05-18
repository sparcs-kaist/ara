from django.db import models

from django_mysql.models import JSONField

from apps.core.classes.model import MetaInfoModel


class DocumentUpdateLog(MetaInfoModel):
    class Meta:
        verbose_name = '문서 수정 내역'
        verbose_name_plural = '문서 수정 내역'

    previous_document = JSONField(
        verbose_name='수정 이전 문서',
    )

    # FK Fields
    created_on = models.ForeignKey(
        to='core.Document',
        db_index=True,
        related_name='update_logs',
        verbose_name='수정 대상 문서',
    )
