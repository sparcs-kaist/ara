from rest_framework import routers

from apps.core.views.viewsets import *

router = routers.SimpleRouter()


router.register(
    prefix=r'categories',
    viewset=CategoryViewSet,
)

router.register(
    prefix=r'articles',
    viewset=ArticleViewSet,
)
