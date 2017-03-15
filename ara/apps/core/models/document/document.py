from django.db import models

from apps.core.classes.model import MetaInfoModel


class Document(MetaInfoModel):
    class Meta:
        verbose_name = '문서'
        verbose_name_plural = '문서'

    content = models.TextField(
        verbose_name='본문',
    )

    # Meta Fields
    is_anonymous = models.BooleanField(
        default=False,
        verbose_name='익명',
    )
    is_content_erotic = models.BooleanField(
        default=False,
        verbose_name='성인/음란성 내용',
    )
    is_content_social = models.BooleanField(
        default=False,
        verbose_name='정치/사회성 내용',
    )
    use_signature = models.BooleanField(
        default=True,
        verbose_name='서명 사용',
    )


class Article(Document):
    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = '게시물'

    title = models.CharField(
        max_length=32,
        verbose_name='제목',
    )

    # FK Fields
    categories = models.ManyToManyField(
        to='core.Category',
        db_index=True,
        related_name='articles',
        verbose_name='분류 목록',
    )
    created_by = models.ForeignKey(
        to='session.UserProfile',
        db_index=True,
        related_name='articles',
        verbose_name='작성자',
    )

    def __str__(self):
        if self.is_anonymous:
            return '{title} - {created_by}'.format(
                title=self.title[:16],
                created_by='anonymous',
            )

        else:
            return '{title} - {created_by}'.format(
                title=self.title[:16],
                created_by=self.created_by,
            )


class BestArticle(MetaInfoModel):
    class Meta:
        verbose_name = '베스트 게시물'
        verbose_name_plural = '베스트 게시물'

    # FK Fields
    article = models.OneToOneField(
        to='core.Article',
        db_index=True,
        related_name='best',
        verbose_name='원본 게시물',
    )


class Comment(Document):
    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글'

    # FK Fields
    created_on = models.ForeignKey(
        to='core.Document',
        db_index=True,
        related_name='comments',
        verbose_name='상위 문서',
    )
    created_by = models.ForeignKey(
        to='session.UserProfile',
        db_index=True,
        related_name='comments',
        verbose_name='작성자',
    )

    def __str__(self):
        if self.is_anonymous:
            return '{content} - {created_by}'.format(
                content=self.title[:16],
                created_by='anonymous',
            )

        else:
            return '{content} - {created_by}'.format(
                content=self.title[:16],
                created_by=self.created_by,
            )


class BestComment(MetaInfoModel):
    class Meta:
        verbose_name = '베스트 댓글'
        verbose_name_plural = '베스트 댓글'

    # FK Fields
    comment = models.OneToOneField(
        to='core.Comment',
        db_index=True,
        related_name='best',
        verbose_name='원본 댓글',
    )
