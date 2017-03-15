from django.db import models

from apps.core.classes.model import MetaInfoModel


class UserProfile(MetaInfoModel):
    class Meta:
        verbose_name = '회원 정보'
        verbose_name_plural = '회원 정보'

    nick = models.CharField(
        unique=True,
        max_length=32,
        verbose_name='닉네임',
    )

    # FK Fields
    user = models.OneToOneField(
        to='auth.User',
        primary_key=True,
        related_name='profile',
        verbose_name='회원 계정',
    )

    def __str__(self):
        return '{nick}({user})'.format(
            nick=self.nick,
            user=self.user,
        )
