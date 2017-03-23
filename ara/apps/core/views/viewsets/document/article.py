from rest_framework import viewsets, permissions

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import Article
from apps.core.serializers.document.article import ArticleSafeMethodSerializer, ArticleCreateMethodSerializer, ArticleUpdateMethodSerializer
from apps.core.backends.category import CategoryFilterBackend


class ArticleViewSet(DebugModeAuthMixin, viewsets.ModelViewSet):
    queryset = Article.objects.select_related('created_by').prefetch_related('comments', 'categories')
    safe_method_serializer_class = ArticleSafeMethodSerializer
    unsafe_method_serializer_class = {
        'create': ArticleCreateMethodSerializer,
        'update': ArticleUpdateMethodSerializer,
        'partial_update': ArticleUpdateMethodSerializer,
    }
    filter_backends = (
        CategoryFilterBackend,
    )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.safe_method_serializer_class

        else:
            return self.unsafe_method_serializer_class[self.action]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user.profile,
        )
