# Third-Party
from rest_framework import serializers

# Local Django
from core.serializers import SocialAccountSerializer
from speaker.models import Speaker, SpeakerSocialAccount


class SpeakerSocialAccountSerializer(serializers.ModelSerializer):
    account = SocialAccountSerializer(read_only=True)

    class Meta:
        model = SpeakerSocialAccount
        fields = ('account', 'url', 'is_active')


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('first_name', 'last_name', 'image', 'is_active')

    def get_image(self, obj):
        url = ""
        if obj.image:
            request = self.context.get('request')
            url = request.build_absolute_uri(obj.image.url)

        return url


class SpeakerListSerializer(SpeakerSerializer):
    pass


class SpeakerRetrieveSerializer(SpeakerSerializer):
    social_accounts = SpeakerSocialAccountSerializer(
        read_only=True, many=True, source='speakersocialaccount_set')

    class Meta:
        model = Speaker
        fields = (
            'first_name', 'last_name', 'email', 'image', 'company', 'company_url', 'position',
            'social_accounts' ,'is_active'
        )
