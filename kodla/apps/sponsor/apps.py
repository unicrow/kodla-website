# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SponsorConfig(AppConfig):
    name = 'sponsor'
    verbose_name = _('Sponsor')
