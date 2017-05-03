# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HackathonConfig(AppConfig):
    name = 'hackathon'
    verbose_name = _('Hackathon')
