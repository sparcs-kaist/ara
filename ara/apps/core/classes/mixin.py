from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import viewsets


class DebugModeAuthMixin(viewsets.GenericViewSet):
    def dispatch(self, request, *args, **kwargs):
        if settings.DEBUG:
            if request.GET.get('user_id'):
                request.user = User.objects.get(username=request.GET['user_id'])

            elif request.GET.get('user_username'):
                request.user = User.objects.get(username=request.GET['user_username'])

        return super(DebugModeAuthMixin, self).dispatch(request, *args, **kwargs)
