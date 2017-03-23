from rest_framework import viewsets

from apps.core.classes.mixin import DebugModeAuthMixin
from apps.core.models import Category
from apps.core.serializers.category import CategorySerializer


class CategoryViewSet(DebugModeAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
