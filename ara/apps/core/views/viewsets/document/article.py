from rest_framework import viewsets

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import Article
from apps.core.serializers.document.article import ArticleSerializer


class ArticleViewSet(DebugModeAuthMixin, viewsets.ModelViewSet):
    queryset = Article.objects.select_related('created_by').prefetch_related('comments', 'categories')
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user.profile,
        )
