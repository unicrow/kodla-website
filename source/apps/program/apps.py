# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProgramConfig(AppConfig):
    name = 'program'
    verbose_name = _('Program')
