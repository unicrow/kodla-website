# Local Django
from ..secrets import GOOGLE_MAPS_API_KEY


GEOPOSITION_GOOGLE_MAPS_API_KEY = GOOGLE_MAPS_API_KEY

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 6,
    'center': {'lat': 41, 'lng': 39.71}
}

GEOPOSITION_MARKER_OPTIONS = {
    'position': {'lat': 41, 'lng': 39.71}
}
