from rest_framework import viewsets

from apps.core.models import Category
from apps.core.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
