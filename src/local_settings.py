# This file is only provided for testing!
# ColdFront Plugin Cloud is only imported as a utility to make use of its
# testing classes and functions and is not required for the operation
# of this plugin.
import os
import pkgutil

from coldfront.config.settings import *
from django.conf import settings

plugin_cloud = pkgutil.get_loader('coldfront_plugin_cloud.config')
include(plugin_cloud.get_filename())

plugin_api = pkgutil.get_loader('coldfront_plugin_api.config')
include(plugin_api.get_filename())


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

if os.getenv('PLUGIN_AUTH_OIDC') == 'True':
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
        'mozilla_django_oidc.contrib.drf.OIDCAuthentication',
    )
