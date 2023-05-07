from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class DisableCSRFOnDev(MiddlewareMixin):
    def process_request(self, request):
        attr = '_dont_enforce_csrf_checks'

        if settings.DEV in ["dev", "stage"]:
            setattr(request, attr, True)
