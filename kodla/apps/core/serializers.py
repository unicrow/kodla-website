# Third-Party
from rest_framework import serializers

# Local Django
from core.models import SocialAccount


class SocialAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialAccount
        fields = ('name', 'style_id', 'style_class')
