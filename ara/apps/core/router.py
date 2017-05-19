from rest_framework import routers

from apps.core.views.viewsets import *

router = routers.SimpleRouter()


# CategoryViewSet

router.register(
    prefix=r'categories',
    viewset=CategoryViewSet,
)


# ArticleViewSet

router.register(
    prefix=r'articles',
    viewset=ArticleViewSet,
)


# CategoryNestedArticleViewSet

router.register(
    prefix=r'categories/(?P<category_id>\d+)/articles',
    viewset=ArticleViewSet,
)


# ArticleNestedDocumentVoteViewSet

router.register(
    prefix=r'articles/(?P<article_id>\d+)/votes',
    viewset=DocumentVoteViewSet,
)


# ArticleNestedDocumentUpdateLogViewSet

router.register(
    prefix=r'articles/(?P<article_id>\d+)/update_logs',
    viewset=DocumentUpdateLogViewSet,
)
# CommentViewSet
router.register(
    prefix=r'articles/(?P<article_no>[0-9]+)/comments',
    viewset=CommentViewSet,
)

router.register(
    prefix=r'articles/(?P<article_no>[0-9]+)/comments/(?P<comment_no>[0-9]+)/comments',
    viewset=CommentViewSet
)


