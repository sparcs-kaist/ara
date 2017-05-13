from rest_framework import viewsets, permissions

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import Comment,Document
from apps.core.serializers.document.comment import CommentSafeMethodSerializer, CommentCreateMethodSerializer, CommentUpdateMethodSerializer
#from apps.core.backends.category import CategoryFilterBackend


class CommentViewSet(DebugModeAuthMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('created_by','created_on')
    safe_method_serializer_class = CommentSafeMethodSerializer
    unsafe_method_serializer_class = {
        'create': CommentCreateMethodSerializer,
        'update': CommentUpdateMethodSerializer,
        'partial_update': CommentUpdateMethodSerializer,
    }
    #filter_backends = (
    #    CategoryFilterBackend,
    #)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.safe_method_serializer_class

        else:
            return self.unsafe_method_serializer_class[self.action]

    def perform_create(self, serializer):
    
        article_no = int(self.kwargs['num'])
        parent_document = Document.objects.get(id=article_no)
        serializer.save(
            created_by=self.request.user.profile,
            created_on=parent_document,
        )
