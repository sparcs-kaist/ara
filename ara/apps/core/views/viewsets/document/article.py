from django.db import transaction

from rest_framework import viewsets

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.classes.pagination import PageNumberPagination
from apps.core.models import Article, DocumentUpdateLog
from apps.core.serializers.document.article import ArticleSafeMethodSerializer, ArticleCreateMethodSerializer, ArticleUpdateMethodSerializer
from apps.core.backends.category import CategoryFilterBackend


class ArticleViewSet(DebugModeAuthMixin, viewsets.ModelViewSet):
    queryset = Article.objects.select_related('created_by').prefetch_related('comments', 'categories')
    pagination_class = PageNumberPagination
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
        if self.action in self.unsafe_method_serializer_class.keys():
            return self.unsafe_method_serializer_class[self.action]

        return self.safe_method_serializer_class

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user.profile,
        )

    def perform_update(self, serializer):
        article = self.get_object()

        update_log = DocumentUpdateLog(
            previous_document=ArticleSafeMethodSerializer(article).data,
            created_on=article,
        )

        with transaction.atomic():
            super(ArticleViewSet, self).perform_update(serializer=serializer)

            update_log.save()
