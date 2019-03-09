# Third-Party
from rest_framework import serializers

# Local Django
from program.models import Program, ProgramContent
from speaker.serializers import SpeakerListSerializer


class ProgramContentSerializer(serializers.ModelSerializer):
    presentation_document = serializers.SerializerMethodField()
    speakers = SpeakerListSerializer(read_only=True, many=True)

    class Meta:
        model = ProgramContent
        fields = (
            'subject', 'annotation', 'presentation_url', 'presentation_document', 'start_time', 'end_time',
            'speakers',
        )

    def get_presentation_document(self, obj):
        url = ""
        if obj.presentation_document:
            request = self.context.get('request')
            url = request.build_absolute_uri(obj.presentation_document.url)

        return url


class ProgramSerializer(serializers.ModelSerializer):
    contents = ProgramContentSerializer(read_only=True, many=True, source='programcontent_set')

    class Meta:
        model = Program
        fields = ('date', 'contents', 'is_active')
