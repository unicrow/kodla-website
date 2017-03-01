# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SpeakerConfig(AppConfig):
    name = 'speaker'
    verbose_name = _('Speaker')
