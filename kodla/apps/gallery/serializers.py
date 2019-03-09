# Third-Party
from rest_framework import serializers

# Local Django
from gallery.models import Gallery, GalleryContent


class GalleryContentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryContent
        fields = ('image', 'is_active')

    def get_image(self, obj):
        url = ""
        if obj.image:
            request = self.context.get('request')
            url = request.build_absolute_uri(obj.image.url)

        return url


class GallerySerializer(serializers.ModelSerializer):
    contents = GalleryContentSerializer(read_only=True, many=True, source='gallerycontent_set')

    class Meta:
        model = Gallery
        fields = ('name', 'tag', 'url', 'contents', 'is_active')
