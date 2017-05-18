from django.db import models

from apps.core.classes.model import MetaInfoModel


class DocumentVote(MetaInfoModel):
    class Meta:
        verbose_name = '문서 투표'
        verbose_name_plural = '문서 투표'

    is_up = models.BooleanField(
        verbose_name='투표 내용',
    )

    # FK Fields
    created_on = models.ForeignKey(
        to='core.Document',
        db_index=True,
        related_name='votes',
        verbose_name='상위 문서',
    )
    created_by = models.ForeignKey(
        to='session.UserProfile',
        db_index=True,
        related_name='votes',
        verbose_name='작성자',
    )
