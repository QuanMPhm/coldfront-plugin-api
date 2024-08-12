import os
import logging

from django_scim.middleware import SCIMAuthCheckMiddleware
from mozilla_django_oidc.contrib.drf import OIDCAuthentication

logger = logging.getLogger(__name__)


class SCIMColdfrontAuthCheckMiddleware(SCIMAuthCheckMiddleware):
    def process_request(self, request):
        if not request.user or not request.user.is_authenticated:
            # PLUGIN_AUTH_OIDC implies DRF OIDC backend is configured
            if os.getenv("PLUGIN_AUTH_OIDC") == "True":
                oidc_auth_obj = OIDCAuthentication()
                request.user = oidc_auth_obj.authenticate(request)
        return super().process_request(request)
