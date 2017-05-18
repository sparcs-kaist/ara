from rest_framework import viewsets

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import DocumentUpdateLog
from apps.core.serializers.document.update_log import DocumentUpdateLogSerializer


class DocumentUpdateLogViewSet(DebugModeAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = DocumentUpdateLog.objects.all()
    serializer_class = DocumentUpdateLogSerializer

    def get_queryset(self):
        queryset = super(DocumentUpdateLogViewSet, self).get_queryset()

        if self.kwargs.get('article_id'):
            queryset = queryset.filter(created_on_id=self.kwargs['article_id'])

        return queryset
