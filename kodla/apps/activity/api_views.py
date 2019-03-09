# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from activity.models import Activity
from activity.serializers import (
    ActivitySerializer, ActivityListSerializer, ActivityRetrieveSerializer
)


class ActivityViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Activity.objects.filter(is_active=True)
    lookup_field = 'year'

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivityListSerializer
        elif self.action == 'retrieve':
            return ActivityRetrieveSerializer
        else:
            return ActivitySerializer

    def get_authenticators(self):
        authentication_classes = ()
        return [auth() for auth in authentication_classes]

    def get_permissions(self):
        permission_classes = []
        return [permission() for permission in permission_classes]
