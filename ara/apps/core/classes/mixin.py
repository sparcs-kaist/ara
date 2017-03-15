from django.conf import settings
from django.contrib.auth.models import User


class DebugModeAuthMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if settings.DEBUG:
            if request.GET.get('username'):
                request.user = User.objects.get(username=request.GET['username'])

            else:
                request.user = User.objects.get(pk=1)

        return super(DebugModeAuthMixin, self).dispatch(request, *args, **kwargs)
