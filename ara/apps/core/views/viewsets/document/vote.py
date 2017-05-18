from rest_framework import mixins, viewsets

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import DocumentVote
from apps.core.serializers.document.vote import DocumentVoteSerializer, DocumentVoteCreateMethodSerializer, DocumentVoteUpdateMethodSerializer


class DocumentVoteViewSet(DebugModeAuthMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = DocumentVote.objects.all()
    safe_method_serializer_class = DocumentVoteSerializer
    unsafe_method_serializer_class = {
        'create': DocumentVoteCreateMethodSerializer,
        'update': DocumentVoteUpdateMethodSerializer,
        'partial_update': DocumentVoteUpdateMethodSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.unsafe_method_serializer_class.keys():
            return self.unsafe_method_serializer_class[self.action]

        return self.safe_method_serializer_class
