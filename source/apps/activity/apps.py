# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    name = 'activity'
    verbose_name = _('Activity')
