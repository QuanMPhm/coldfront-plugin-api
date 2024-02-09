from rest_framework import routers, viewsets
from rest_framework.permissions import IsAdminUser

from coldfront.core.allocation.models import Allocation
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django_scim import views as scim_views

from coldfront_plugin_api import auth, serializers
from coldfront_plugin_api.scim_v2 import groups, users


class AllocationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AllocationSerializer
    authentication_classes = auth.AUTHENTICATION_CLASSES
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Allocation.objects.filter(status__name='Active')

        if self.request.query_params.get('all') == 'true':
            queryset = Allocation.objects.all()

        return queryset


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'allocations', AllocationViewSet, basename='api-allocation')

urlpatterns = router.urls

urlpatterns += [
    path('scim/v2/', include('django_scim.urls'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
