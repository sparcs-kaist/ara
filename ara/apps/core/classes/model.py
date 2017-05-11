import datetime

from django.db import models
from django.utils import timesince


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
        auto_now=True,
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

    @property
    def since_created_at(self):
        return self.since_datetime(self.created_at)

    @property
    def since_updated_at(self):
        return self.since_datetime(self.updated_at)

    @property
    def since_deleted_at(self):
        return self.since_datetime(self.deleted_at)

    @property
    def display_created_at(self):
        return self.display_datetime(self.created_at)

    @property
    def display_updated_at(self):
        return self.display_datetime(self.updated_at)

    @property
    def display_deleted_at(self):
        return self.display_datetime(self.deleted_at)

    @staticmethod
    def since_datetime(refer_dt):
        if not refer_dt:
            return None

        return timesince.timesince(refer_dt).split(",")[0]

    @staticmethod
    def display_datetime(refer_dt):
        if not refer_dt:
            return None

        refer_dt_y, refer_dt_m, refer_dt_d = refer_dt.isocalendar()
        today_dt_y, today_dt_m, today_dt_d = datetime.date.today().isocalendar()

        if (refer_dt_y, refer_dt_m, refer_dt_d) == (today_dt_y, today_dt_m, today_dt_d):
            return refer_dt.strftime('%H:%M')

        elif refer_dt_y == today_dt_y:
            return refer_dt.strftime('%m-%d %H:%M')

        else:
            return refer_dt.strftime('%y-%m-%d %H:%M')
