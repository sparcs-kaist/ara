from django.db import models

from apps.core.classes.model import MetaInfoModel


class Category(MetaInfoModel):
    class Meta:
        verbose_name = '게시물 분류'
        verbose_name_plural = '게시물 분류'

    slug = models.SlugField(
        unique=True,
        max_length=32,
        verbose_name='URL 표현',
    )
    ko_name = models.CharField(
        unique=True,
        max_length=32,
        verbose_name='국문 분류 명칭',
    )
    en_name = models.CharField(
        unique=True,
        max_length=32,
        verbose_name='영문 분류 명칭',
    )
    ko_description = models.CharField(
        max_length=256,
        verbose_name='국문 분류 설명'
    )
    en_description = models.CharField(
        max_length=256,
        verbose_name='영문 분류 설명'
    )

    def __str__(self):
        return '[{slug}] {ko_name}'.format(
            slug=self.slug,
            ko_name=self.ko_name,
        )
