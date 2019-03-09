import collections

# Third-Party
from rest_framework import serializers

# Local Django
from activity.models import Activity, ActivitySocialAccount, ActivityMap
from core.serializers import SocialAccountSerializer
from gallery.serializers import GallerySerializer
from program.serializers import ProgramSerializer
from speaker.serializers import SpeakerRetrieveSerializer


class ActivityMapSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityMap
        fields = ('coordinates', 'description', 'is_active')


class ActivitySocialAccountSerializer(serializers.ModelSerializer):
    account = SocialAccountSerializer(read_only=True)

    class Meta:
        model = ActivitySocialAccount
        fields = ('account', 'url', 'is_active')


class ActivitySerializer(serializers.ModelSerializer):
    sponsor_document = serializers.SerializerMethodField()
    social_accounts = ActivitySocialAccountSerializer(
        read_only=True, many=True, source='activitysocialaccount_set')

    class Meta:
        model = Activity
        fields = (
            'id', 'year', 'email', 'short_description', 'description', 'register_url', 'sponsor_document',
            'social_accounts', 'is_active'
        )
        extra_kwargs = {
            'url': {'lookup_field': 'year'}
        }

    def get_sponsor_document(self, obj):
        url = ""
        document = obj.activitydocument_set.filter(is_active=True).first()
        if document is not None:
            request = self.context.get('request')
            url = request.build_absolute_uri(document.document.url)

        return url


class ActivityListSerializer(ActivitySerializer):

    class Meta:
        model = Activity
        fields = (
            'id', 'year', 'email', 'short_description', 'description', 'register_url', 'sponsor_document',
            'social_accounts', 'is_active'
        )


class ActivityRetrieveSerializer(ActivitySerializer):
    maps = ActivityMapSerializer(read_only=True, many=True, source='activitymap_set')
    sponsors = serializers.SerializerMethodField()
    programs = ProgramSerializer(read_only=True, many=True, source='program_set')
    speakers = SpeakerRetrieveSerializer(read_only=True, many=True)
    gallery = GallerySerializer(read_only=True, many=True, source='gallery_set')

    class Meta:
        model = Activity
        fields = (
            'id', 'year', 'email', 'is_active', 'short_description', 'description', 'register_url',
            'sponsor_document', 'address', 'transportation', 'accommodation', 'contact_info',
            'social_accounts', 'sponsors', 'programs', 'speakers', 'maps', 'gallery'
        )

    def get_sponsors(self, obj):
        request = self.context.get('request')
        activity_sponsors = collections.OrderedDict()
        sponsors = obj.activitysponsor_set \
            .filter(is_active=True, sponsor_type__is_active=True) \
            .order_by('sponsor_type', 'order_id')
        for sponsor in sponsors:
            data = collections.OrderedDict()
            data.update({
                'name': sponsor.sponsor.name,
                'url': sponsor.sponsor.url,
                'logo': request.build_absolute_uri(sponsor.sponsor.logo.url)
            })
            activity_sponsors.setdefault(sponsor.sponsor_type.name, []) \
                .append(data)

        return activity_sponsors
